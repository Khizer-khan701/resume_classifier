from .repositories import UserProfileRepository

def user_profile(request):
    """
    Context processor to make the Firestore UserProfile available in all templates.
    """
    if request.user.is_authenticated:
        try:
            repo = UserProfileRepository()
            uid = request.user.username  # Firebase UID
            profiles = repo.query('user_id', '==', uid)
            if profiles:
                return {'user_profile': profiles[0]}
        except Exception:
            pass
    return {'user_profile': None}
