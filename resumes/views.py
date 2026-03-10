from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from datetime import datetime

from .storage import LocalDocumentStorage
from .repositories import ResumeRepository
from ai_analysis.tasks import process_resume_task

@login_required
def upload_view(request):
    """View to handle drag-and-drop file uploads."""
    if request.method == 'POST':
        # Accept either standard form submission or AJAX form data
        uploaded_file = request.FILES.get('resume_file')
        
        if not uploaded_file:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': 'No file uploaded'}, status=400)
            messages.error(request, 'Please select a file to upload.')
            return redirect('resumes:upload')
            
        # Basic validation
        if not uploaded_file.name.lower().endswith(('.pdf', '.docx', '.doc')):
            error_msg = 'Only PDF and DOCX files are supported.'
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': error_msg}, status=400)
            messages.error(request, error_msg)
            return redirect('resumes:upload')
            
        uid = request.user.username
        storage = LocalDocumentStorage()
        
        try:
            # 1. Save file locally
            file_path = storage.save_file(uploaded_file, uid)
            
            # 2. Record in Firestore
            repo = ResumeRepository()
            resume_data = {
                'user_id': uid,
                'original_filename': uploaded_file.name,
                'storage_path': file_path,
                'upload_date': datetime.utcnow().isoformat(),
                'status': 'pending', # pending -> processing -> completed/failed
            }
            
            resume_doc = repo.create(resume_data)
            resume_id = resume_doc['id']
            
            # 3. Trigger Background Task stringing parsing + AI analysis
            process_resume_task.delay(resume_id)
            
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success', 
                    'message': 'File uploaded successfully. Processing started.',
                    'resume_id': resume_id,
                    'redirect_url': f'/resumes/{resume_id}/'
                })
                
            messages.success(request, 'Resume uploaded successfully! We are analyzing it now.')
            return redirect('resumes:detail', resume_id=resume_id)
            
        except Exception as e:
            # Check for Celery connection errors specifically for better messaging
            if 'reconnect to the Celery redis' in str(e).lower() or 'connection refused' in str(e).lower():
                error_msg = 'Backend processing system (Redis/Celery) is currently unreachable. Please ensure Docker containers are running.'
            else:
                error_msg = f'Error processing upload: {str(e)}'
                
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'message': error_msg}, status=500)
            messages.error(request, error_msg)
            return redirect('resumes:upload')

    return render(request, 'resumes/upload.html')

@login_required
def resume_list_view(request):
    """List all uploaded resumes for the user."""
    uid = request.user.username
    repo = ResumeRepository()
    
    # Query all resumes for this user, sorted by date in memory (since simple firestore query)
    resumes = repo.query('user_id', '==', uid)
    resumes.sort(key=lambda x: x.get('upload_date', ''), reverse=True)
    
    return render(request, 'resumes/list.html', {'resumes': resumes})

@login_required
def resume_detail_view(request, resume_id):
    """View details and analysis status of a specific resume."""
    uid = request.user.username
    repo = ResumeRepository()
    
    resume = repo.get_by_id(resume_id)
    if not resume or resume.get('user_id') != uid:
        messages.error(request, 'Resume not found or unauthorized.')
        return redirect('resumes:list')
        
    context = {'resume': resume}
    
    if resume.get('status') == 'completed':
        # Fetch the analysis
        from ai_analysis.repositories import ResumeAnalysisRepository
        analysis_repo = ResumeAnalysisRepository()
        analyses = analysis_repo.query('resume_id', '==', resume_id)
        if analyses:
            context['analysis'] = analyses[0]
            
    return render(request, 'resumes/detail.html', context)

@login_required
def delete_resume_view(request, resume_id):
    """Delete a resume, its associated analysis, and the physical file."""
    if request.method == 'POST':
        uid = request.user.username
        resume_repo = ResumeRepository()
        
        resume = resume_repo.get_by_id(resume_id)
        if not resume or resume.get('user_id') != uid:
            messages.error(request, 'Resume not found or unauthorized.')
            return redirect('resumes:list')
            
        try:
            # 1. Delete associated analysis if exists
            from ai_analysis.repositories import ResumeAnalysisRepository
            analysis_repo = ResumeAnalysisRepository()
            analyses = analysis_repo.query('resume_id', '==', resume_id)
            for a in analyses:
                analysis_repo.delete(a['id'])
            
            # 2. Delete physical file
            storage = LocalDocumentStorage()
            storage.delete_file(resume.get('storage_path'))
            
            # 3. Delete resume metadata from Firestore
            resume_repo.delete(resume_id)
            
            messages.success(request, 'Resume deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting resume: {str(e)}')
            
    return redirect('resumes:list')

@login_required
def resume_status_api(request, resume_id):
    """API endpoint for AJAX polling of resume status."""
    uid = request.user.username
    repo = ResumeRepository()
    resume = repo.get_by_id(resume_id)
    
    if not resume or resume.get('user_id') != uid:
        return JsonResponse({'status': 'error', 'message': 'Not found'}, status=404)
        
    return JsonResponse({
        'status': resume.get('status'),
        'id': resume_id
    })

