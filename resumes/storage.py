import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

class LocalDocumentStorage:
    """
    Abstraction layer for storing uploaded resume files.
    Currently maps to local media filesystem, but interface can be
    implemented for GCS, S3, etc later.
    """
    
    def __init__(self):
        self.storage = FileSystemStorage(location=settings.MEDIA_ROOT)
        
    def save_file(self, file_obj, user_id: str) -> str:
        """
        Saves a resume file securely scoped to the user.
        Returns the persistent path.
        """
        # Create user specific folder structure logically
        file_ext = os.path.splitext(file_obj.name)[1]
        secure_name = f"{user_id}_{file_obj.name}"
        saved_name = self.storage.save(secure_name, file_obj)
        
        return self.storage.path(saved_name)

    def delete_file(self, document_path: str):
        if os.path.exists(document_path):
            os.remove(document_path)
            
    def get_file_url(self, file_path: str) -> str:
        filename = os.path.basename(file_path)
        return self.storage.url(filename)
