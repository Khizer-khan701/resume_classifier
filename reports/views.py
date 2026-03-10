from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from resumes.repositories import ResumeRepository
from ai_analysis.repositories import ResumeAnalysisRepository

@login_required
def export_resume_report(request, resume_id):
    """
    Renders a print-friendly analysis report. 
    Users can use native 'Save as PDF' from their browser,
    which is robust and doesn't require heavy dependencies like WeasyPrint.
    """
    uid = request.user.username
    
    resume_repo = ResumeRepository()
    resume = resume_repo.get_by_id(resume_id)
    
    if not resume or resume.get('user_id') != uid:
        return redirect('dashboard:home')
        
    analysis_repo = ResumeAnalysisRepository()
    analyses = analysis_repo.query('resume_id', '==', resume_id)
    
    context = {
        'resume': resume,
        'analysis': analyses[0] if analyses else None
    }
    
    return render(request, 'reports/report_print.html', context)
