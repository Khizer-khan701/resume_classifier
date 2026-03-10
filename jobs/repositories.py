from common.repositories import BaseFirestoreRepository

class GeneratedContentRepository(BaseFirestoreRepository):
    @property
    def collection_name(self) -> str:
        return 'generated_content'
