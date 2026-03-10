from common.repositories import BaseFirestoreRepository

class UserProfileRepository(BaseFirestoreRepository):
    @property
    def collection_name(self) -> str:
        return 'user_profiles'
