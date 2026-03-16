import abc
from typing import Dict, Any, Optional, List
from google.cloud import firestore
import firebase_admin
from firebase_admin import firestore as firebase_firestore

class BaseFirestoreRepository(abc.ABC):
    """
    Abstract base class for Firestore repositories.
    Provides basic CRUD operations for a specific collection.
    """

    @property
    @abc.abstractmethod
    def collection_name(self) -> str:
        """Name of the Firestore collection."""
        pass

    def __init__(self):
        # Ensure Firebase app is initialized before accessing Firestore
        if not firebase_admin._apps:
            # Try to initialize Firebase
            try:
                from firebase_init import initialize_firebase
                success = initialize_firebase()
                if not success:
                    raise RuntimeError(
                        "Firebase Admin SDK could not be initialized. "
                        "Please check your FIREBASE_SERVICE_ACCOUNT_JSON or FIREBASE_CREDENTIALS_PATH settings."
                    )
            except ImportError:
                raise RuntimeError(
                    "Firebase Admin SDK is not initialized and firebase_init module not found."
                )
        self.db: firestore.Client = firebase_firestore.client()
        self.collection: firestore.CollectionReference = self.db.collection(self.collection_name)

    def get_by_id(self, doc_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a document by its ID."""
        doc_ref = self.collection.document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            data = doc.to_dict()
            data['id'] = doc.id
            return data
        return None

    def create(self, data: Dict[str, Any], doc_id: Optional[str] = None) -> Dict[str, Any]:
        """Create a new document. If doc_id is None, an auto-generated ID is used."""
        if doc_id:
            doc_ref = self.collection.document(doc_id)
            doc_ref.set(data)
        else:
            _, doc_ref = self.collection.add(data)
            
        return self.get_by_id(doc_ref.id)

    def update(self, doc_id: str, data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Update an existing document."""
        doc_ref = self.collection.document(doc_id)
        if not doc_ref.get().exists:
            return None
        doc_ref.update(data)
        return self.get_by_id(doc_id)

    def delete(self, doc_id: str) -> bool:
        """Delete a document by its ID."""
        doc_ref = self.collection.document(doc_id)
        if doc_ref.get().exists:
            doc_ref.delete()
            return True
        return False

    def list_all(self, limit: int = 100) -> List[Dict[str, Any]]:
        """List all documents in the collection, up to a limit."""
        docs = self.collection.limit(limit).stream()
        results = []
        for doc in docs:
            data = doc.to_dict()
            data['id'] = doc.id
            results.append(data)
        return results

    def query(self, field: str, operator: str, value: Any, limit: int = 100) -> List[Dict[str, Any]]:
        """
        Query the collection.
        Example operator: '==', '<', '>', 'in', 'array_contains'
        """
        docs = self.collection.where(filter=firestore.FieldFilter(field, operator, value)).limit(limit).stream()
        results = []
        for doc in docs:
            data = doc.to_dict()
            data['id'] = doc.id
            results.append(data)
        return results
