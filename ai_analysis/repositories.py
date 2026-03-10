from common.repositories import BaseFirestoreRepository

class ResumeAnalysisRepository(BaseFirestoreRepository):
    @property
    def collection_name(self) -> str:
        return 'resume_analyses'
