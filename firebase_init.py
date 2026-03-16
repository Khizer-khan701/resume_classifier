import os
import json
import firebase_admin
from firebase_admin import credentials

# Load environment variables from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not available, continue

def initialize_firebase():
    """
    Initialize Firebase Admin SDK with proper fallback logic.
    Returns True if initialized successfully, False otherwise.
    """
    if firebase_admin._apps:
        return True

    firebase_json = os.getenv("FIREBASE_SERVICE_ACCOUNT_JSON")
    firebase_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

    print(f"DEBUG: FIREBASE_SERVICE_ACCOUNT_JSON present: {firebase_json is not None}")
    print(f"DEBUG: FIREBASE_CREDENTIALS_PATH: {firebase_path}")

    try:
        if firebase_json:
            cred_dict = json.loads(firebase_json)
            cred = credentials.Certificate(cred_dict)
            firebase_admin.initialize_app(cred)
            print("Firebase initialized from FIREBASE_SERVICE_ACCOUNT_JSON")
            return True

        elif firebase_path and os.path.exists(firebase_path):
            cred = credentials.Certificate(firebase_path)
            firebase_admin.initialize_app(cred)
            print(f"Firebase initialized from file: {firebase_path}")
            return True

        else:
            print("WARNING: Firebase credentials not found. Firebase features will be disabled.")
            print(f"DEBUG: firebase_path='{firebase_path}', exists={os.path.exists(firebase_path) if firebase_path else 'N/A'}")
            return False

    except Exception as e:
        print(f"Firebase initialization failed: {e}")
        return False