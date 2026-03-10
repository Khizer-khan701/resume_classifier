from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from django.conf import settings
import logging

from .schemas import ParsedResumeOutput

logger = logging.getLogger(__name__)

def get_llm():
    """Initialize the OpenAI Chat model."""
    api_key = getattr(settings, 'OPENAI_API_KEY', None)
    if not api_key:
        logger.warning("OPENAI_API_KEY not set. LangChain operations will fail.")
    return ChatOpenAI(temperature=0.1, model="gpt-4o-mini", api_key=api_key)

def analyze_resume_text(resume_text: str) -> dict:
    """
    Run the LangChain extraction and analysis pipeline on raw resume text.
    Uses OpenAI's native Structured Outputs for maximum speed and reliability.
    """
    llm = get_llm()
    
    # Use native structured output - much faster than manual parsing
    structured_llm = llm.with_structured_output(ParsedResumeOutput)
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert technical recruiter. Extract structured info from the resume accurately and concisely."),
        ("human", "Analyze this resume text:\n\n{resume_text}")
    ])
    
    chain = prompt | structured_llm
    
    try:
        # Run inference
        result = chain.invoke({"resume_text": resume_text})
        # result is already a ParsedResumeOutput object
        return result.model_dump()
        
    except Exception as e:
        logger.error(f"Error in LangChain analysis: {str(e)}")
        raise
