from common.repositories import BaseFirestoreRepository

class ResumeRepository(BaseFirestoreRepository):
    @property
    def collection_name(self) -> str:
        return 'resumes'

class ParsedResumeDataRepository(BaseFirestoreRepository):
    @property
    def collection_name(self) -> str:
        return 'parsed_resume_data'
