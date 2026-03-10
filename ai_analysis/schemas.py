from pydantic import BaseModel, Field
from typing import List, Optional

class ResumeActionableFeedback(BaseModel):
    summary_improvement: str = Field(description="Suggestion to improve the professional summary")
    experience_bullets_improvement: str = Field(description="Suggestion to improve work experience bullet points (add metrics, action verbs, etc)")
    missing_keywords: List[str] = Field(description="Important industry keywords missing from the resume")
    formatting_suggestions: str = Field(description="Tips for better formatting and readability")

class JobRoleMatch(BaseModel):
    role_name: str = Field(description="Standardized name of the job role (e.g. Frontend Developer, Data Scientist)")
    match_percentage: int = Field(description="Estimated match percentage (0-100) based on skills and experience")
    missing_skills: List[str] = Field(description="Key skills required for this role that are missing from the resume")

class ParsedResumeOutput(BaseModel):
    first_name: str = Field(description="Candidate's first name")
    last_name: str = Field(description="Candidate's last name")
    email: Optional[str] = Field(description="Candidate's email if found, else None")
    phone: Optional[str] = Field(description="Candidate's phone number if found, else None")
    
    technical_skills: List[str] = Field(description="List of hard technical skills, tools, and languages")
    soft_skills: List[str] = Field(description="List of soft skills")
    
    experience_level: str = Field(description="Classify as: Entry, Junior, Mid, Senior, or Executive")
    ats_score: int = Field(description="Estimated ATS compatibility score (0-100)")
    
    recommended_roles: List[JobRoleMatch] = Field(description="Top 2-3 recommended job roles based on the profile")
    
    improvement_suggestions: ResumeActionableFeedback = Field(description="Actionable feedback to improve the resume")
