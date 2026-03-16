from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.http import JsonResponse
import json
from .repositories import UserProfileRepository
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from firebase_admin import auth

def signup_view(request):
    """Render the signup page with Firebase UI."""
    return render(request, 'accounts/signup.html')

def login_view(request):
    """Render the login page with Firebase UI."""
    return render(request, 'accounts/login.html')

@csrf_exempt
def firebase_login(request):
    """
    Endpoint called by JS after Firebase authenticates the user.
    It verifies the idToken with Firebase Admin SDK, provisions a Django session,
    and optionally creates a Firestore UserProfile.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method"}, status=405)

    try:
        print("CONTENT TYPE:", request.content_type)
        print("BODY:", request.body)
        print("POST DATA:", request.POST)

        data = json.loads(request.body)
        print("JSON DATA:", data)

        id_token = data.get("idToken")
        if not id_token:
            return JsonResponse({"error": "ID token missing"}, status=400)

        # Verify the ID token with Firebase Admin SDK
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token.get("uid")
        email = decoded_token.get("email", "")
        display_name = decoded_token.get("name", "")

        print("DECODED TOKEN:", decoded_token)

        # Authenticate via custom backend
        user = authenticate(request, firebase_uid=uid, email=email)
        if user:
            django_login(request, user)

            # Check / Create User Profile in Firestore
            repo = UserProfileRepository()
            profile = repo.query('user_id', '==', uid)
            if not profile:
                # New user detected
                first_name = display_name.split(' ')[0] if display_name else ''
                last_name = ' '.join(display_name.split(' ')[1:]) if display_name else ''

                repo.create({
                    'user_id': uid,
                    'email': email,
                    'first_name': first_name,
                    'last_name': last_name,
                    'target_job': '',
                    'subscription_tier': 'free',
                })

            return JsonResponse({
                "message": "Login successful",
                "uid": uid
            }, status=200)
        else:
            return JsonResponse({"error": "Authentication failed"}, status=401)
    except Exception as e:
        print("EXCEPTION:", str(e))
        return JsonResponse({"error": str(e)}, status=400)

def logout_view(request):
    """Logout user from Django session."""
    django_logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('accounts:login')

@login_required
def profile_view(request):
    """User profile editing page."""
    uid = request.user.username  # We store Firebase UID in the Django username field
    repo = UserProfileRepository()
    
    try:
        profiles = repo.query('user_id', '==', uid)
        if not profiles:
            messages.error(request, 'Profile not found in Firestore.')
            return redirect('dashboard:home')
            
        profile = profiles[0]
        
        if request.method == 'POST':
            target_job = request.POST.get('target_job')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            
            repo.update(profile['id'], {
                'target_job': target_job,
                'first_name': first_name,
                'last_name': last_name
            })
            
            messages.success(request, 'Profile updated successfully.')
            return redirect('accounts:profile')
            
        return render(request, 'accounts/profile.html', {'profile': profile})
    except Exception as e:
        messages.error(request, f'Database Error: {str(e)}')
        return redirect('dashboard:home')
