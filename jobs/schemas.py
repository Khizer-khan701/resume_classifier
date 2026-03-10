from pydantic import BaseModel, Field
from typing import List

class CoverLetterOutput(BaseModel):
    subject: str = Field(description="Suggested email subject line")
    body: str = Field(description="The full content of the cover letter, formatted with paragraphs")
    match_score: int = Field(description="Estimated match score (0-100) of the resume against the job description")
    key_selling_points: List[str] = Field(description="3-4 key bullet points why the candidate is a good fit")

class InterviewQuestion(BaseModel):
    question: str = Field(description="The interview question")
    intent: str = Field(description="What the interviewer is trying to evaluate")
    suggested_answer_strategy: str = Field(description="How the candidate should approach answering based on their resume")

class InterviewPrepOutput(BaseModel):
    technical_questions: List[InterviewQuestion] = Field(description="3-5 technical or role-specific questions")
    behavioral_questions: List[InterviewQuestion] = Field(description="3-5 behavioral questions tailored to the resume and job")
    weakness_questions: List[InterviewQuestion] = Field(description="1-2 questions addressing potential weaknesses or gaps in the resume compared to the job")

class MatchScoreOutput(BaseModel):
    match_percentage: int = Field(description="Match percentage (0-100) of how well the resume fits the job description")
    matching_skills: List[str] = Field(description="List of skills and qualifications found in both the resume and JD")
    missing_keywords: List[str] = Field(description="Crucial skills, tools, or keywords mentioned in the JD that are MISSING in the resume")
    improvement_advice: List[str] = Field(description="3-4 actionable tips for the candidate to update their resume to better fit this specific role")
