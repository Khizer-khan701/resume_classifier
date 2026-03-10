from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from resumes.repositories import ResumeRepository
from ai_analysis.repositories import ResumeAnalysisRepository
from accounts.repositories import UserProfileRepository

@login_required
def home_view(request):
    """Render the user dashboard home with actual stats."""
    uid = request.user.username
    resume_repo = ResumeRepository()
    analysis_repo = ResumeAnalysisRepository()
    user_repo = UserProfileRepository()
    
    try:
        resumes = resume_repo.query('user_id', '==', uid)
        resumes.sort(key=lambda x: x.get('upload_date', ''), reverse=True)
        
        analyses = analysis_repo.query('user_id', '==', uid)
        
        total_resumes = len(resumes)
        avg_score = 0
        best_score = 0
        skills_count = 0
        
        if len(analyses) > 0:
            scores = [a.get('ats_score', 0) for a in analyses]
            avg_score = int(sum(scores) / len(analyses))
            best_score = max(scores)
            
            # Count unique skills across all analyses
            all_skills = set()
            for a in analyses:
                structured = a.get('structured_data', {})
                all_skills.update(structured.get('technical_skills', []))
                all_skills.update(structured.get('soft_skills', []))
            skills_count = len(all_skills)
            
        recent_resumes = resumes[:5]
        # Attach analysis score to each recent resume for the chart
        for r in recent_resumes:
            r_analysis = next((a for a in analyses if a.get('resume_id') == r.get('id')), None)
            r['ats_score'] = r_analysis.get('ats_score', 0) if r_analysis else 0
        
        # Fetch User Profile for display name
        profiles = user_repo.query('user_id', '==', uid)
        user_profile = profiles[0] if profiles else None
        
        context = {
            'total_resumes': total_resumes,
            'avg_score': avg_score,
            'best_score': best_score,
            'skills_count': skills_count,
            'recent_resumes': recent_resumes,
            'profile': user_profile
        }
        
        return render(request, 'dashboard/home.html', context)
    except Exception as e:
        return render(request, 'dashboard/home.html', {'error': str(e)})
