from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from ai_analysis.chains import get_llm
import logging

from .schemas import CoverLetterOutput, InterviewPrepOutput, MatchScoreOutput

logger = logging.getLogger(__name__)

def generate_cover_letter(resume_text: str, job_description: str) -> dict:
    """Generate a cover letter based on a resume and job description."""
    llm = get_llm()
    parser = PydanticOutputParser(pydantic_object=CoverLetterOutput)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert career coach and copywriter. Your task is to write a compelling, professional cover letter for a candidate based on their resume and a target job description. The cover letter should highlight the most relevant skills.\n\n{format_instructions}"),
        ("human", "CANDIDATE RESUME:\n{resume_text}\n\nTARGET JOB DESCRIPTION:\n{job_description}")
    ])
    
    chain = prompt | llm | parser
    
    try:
        result = chain.invoke({
            "resume_text": resume_text,
            "job_description": job_description,
            "format_instructions": parser.get_format_instructions()
        })
        return result.model_dump()
    except Exception as e:
        logger.error(f"Error generating cover letter: {str(e)}")
        raise

def generate_interview_prep(resume_text: str, job_description: str) -> dict:
    """Generate custom interview questions based on resume and job description."""
    llm = get_llm()
    parser = PydanticOutputParser(pydantic_object=InterviewPrepOutput)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert technical interviewer and hiring manager. Your task is to generate highly tailored interview questions for a candidate based on their resume and the job description they are applying for. Formulate questions that probe their specific experiences and potential skill gaps relative to the job.\n\n{format_instructions}"),
        ("human", "CANDIDATE RESUME:\n{resume_text}\n\nTARGET JOB DESCRIPTION:\n{job_description}")
    ])
    
    chain = prompt | llm | parser
    
    try:
        result = chain.invoke({
            "resume_text": resume_text,
            "job_description": job_description,
            "format_instructions": parser.get_format_instructions()
        })
        return result.model_dump()
    except Exception as e:
        logger.error(f"Error generating interview prep: {str(e)}")
        raise

def generate_match_score(resume_text: str, job_description: str) -> dict:
    """Compare a resume against a job description and return a detailed match score."""
    llm = get_llm()
    parser = PydanticOutputParser(pydantic_object=MatchScoreOutput)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert ATS (Applicant Tracking System) specialist and career consultant. Your task is to analyze a candidate's resume against a specific job description. Calculate a realistic match percentage (0-100), identify exactly which crucial skills from the JD are missing in the resume, and provide actionable advice to improve the match.\n\n{format_instructions}"),
        ("human", "CANDIDATE RESUME:\n{resume_text}\n\nTARGET JOB DESCRIPTION:\n{job_description}")
    ])
    
    chain = prompt | llm | parser
    
    try:
        result = chain.invoke({
            "resume_text": resume_text,
            "job_description": job_description,
            "format_instructions": parser.get_format_instructions()
        })
        return result.model_dump()
    except Exception as e:
        logger.error(f"Error generating match score: {str(e)}")
        raise
