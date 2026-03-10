import logging
from celery import shared_task
from datetime import datetime

from resumes.repositories import ResumeRepository
from resumes.parsers import extract_text
from ai_analysis.repositories import ResumeAnalysisRepository
from ai_analysis.chains import analyze_resume_text

logger = logging.getLogger(__name__)

@shared_task
def process_resume_task(resume_id: str):
    """
    Background task to parse the resume file,
    extract text, run LangChain pipelines, and save results.
    """
    resume_repo = ResumeRepository()
    analysis_repo = ResumeAnalysisRepository()
    
    # 1. Fetch Resume Metadata
    resume = resume_repo.get_by_id(resume_id)
    if not resume:
        logger.error(f"Cannot process resume {resume_id}: Not found in Firestore")
        return False
        
    try:
        # Mark as processing - Step 1: Extraction
        resume_repo.update(resume_id, {'status': 'extracting_text'})
        logger.info(f"Extracting text from resume {resume_id}")
        
        # 2. Extract Text
        file_path = resume.get('storage_path')
        text = extract_text(file_path)
        
        if not text or len(text.strip()) < 10:
            raise ValueError("No readable text found in the resume file.")

        # Mark as processing - Step 2: AI Analysis
        resume_repo.update(resume_id, {'status': 'ai_analyzing'})
        logger.info(f"Running AI analysis for resume {resume_id}")
        
        # 3. Run AI Analysis via LangChain
        structured_data = analyze_resume_text(text)
        
        # Mark as processing - Step 3: Saving
        resume_repo.update(resume_id, {'status': 'saving_results'})
        
        # 4. Save Results to Firestore
        analysis_data = {
            'resume_id': resume_id,
            'user_id': resume.get('user_id'),
            'parsed_text': text,
            'structured_data': structured_data,
            'ats_score': structured_data.get('ats_score', 0),
            'recommended_roles': structured_data.get('recommended_roles', []),
            'created_at': datetime.utcnow().isoformat()
        }
        
        analysis_repo.create(analysis_data)
        
        # 5. Mark as Completed
        resume_repo.update(resume_id, {'status': 'completed'})
        logger.info(f"Successfully processed resume {resume_id}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to process resume {resume_id}: {str(e)}")
        # Mark as Failed
        resume_repo.update(resume_id, {
            'status': 'failed', 
            'error_message': str(e),
            'failed_at': datetime.utcnow().isoformat()
        })
        return False
