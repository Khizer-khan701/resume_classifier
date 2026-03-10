from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
import uuid

from resumes.repositories import ResumeRepository
from ai_analysis.repositories import ResumeAnalysisRepository
from .repositories import GeneratedContentRepository
from .chains import generate_cover_letter, generate_interview_prep, generate_match_score

@login_required
def tools_home_view(request):
    """Landing page for job helper tools."""
    # Fetch user's analyzed resumes to use as context
    resume_repo = ResumeRepository()
    uid = request.user.username
    resumes = resume_repo.query('user_id', '==', uid)
    # Only show completed resumes
    completed_resumes = [r for r in resumes if r.get('status') == 'completed']
    completed_resumes.sort(key=lambda x: x.get('upload_date', ''), reverse=True)
    
    return render(request, 'jobs/tools.html', {'resumes': completed_resumes})

@login_required
def generate_tool_view(request):
    """Handle generation requests (synchronously for MVP)."""
    if request.method == 'POST':
        tool_type = request.POST.get('tool_type') # 'cover_letter', 'interview', or 'match_score'
        resume_id = request.POST.get('resume_id')
        job_description = request.POST.get('job_description')
        
        if not all([tool_type, resume_id, job_description]):
            messages.error(request, 'Please provide all required fields.')
            return redirect('jobs:tools_home')
            
        # Get resume text
        analysis_repo = ResumeAnalysisRepository()
        analyses = analysis_repo.query('resume_id', '==', resume_id)
        
        if not analyses:
            messages.error(request, 'Selected resume has not been analyzed yet.')
            return redirect('jobs:tools_home')
            
        resume_text = analyses[0].get('parsed_text', '')
        
        uid = request.user.username
        content_repo = GeneratedContentRepository()
        
        try:
            if tool_type == 'cover_letter':
                result = generate_cover_letter(resume_text, job_description)
            elif tool_type == 'interview':
                result = generate_interview_prep(resume_text, job_description)
            elif tool_type == 'match_score':
                result = generate_match_score(resume_text, job_description)
            else:
                messages.error(request, 'Invalid tool type.')
                return redirect('jobs:tools_home')
                
            # Save to Firestore
            doc_data = {
                'user_id': uid,
                'resume_id': resume_id,
                'type': tool_type,
                'content': result,
                'created_at': datetime.utcnow().isoformat()
            }
            saved_doc = content_repo.create(doc_data)
            
            return redirect('jobs:tool_result', doc_id=saved_doc['id'])
            
        except Exception as e:
            messages.error(request, f'Error generating content: {str(e)}')
            return redirect('jobs:tools_home')
            
    return redirect('jobs:tools_home')

@login_required
def tool_result_view(request, doc_id):
    """Display the generated cover letter or interview questions."""
    repo = GeneratedContentRepository()
    doc = repo.get_by_id(doc_id)
    
    if not doc or doc.get('user_id') != request.user.username:
        messages.error(request, 'Document not found.')
        return redirect('jobs:tools_home')
        
    if doc.get('type') == 'cover_letter':
        template_name = 'jobs/cover_letter.html'
    elif doc.get('type') == 'match_score':
        template_name = 'jobs/match_score.html'
    else:
        template_name = 'jobs/interview.html'
    
    return render(request, template_name, {'document': doc})
