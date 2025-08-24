import requests
from django.core.files.storage import Storage
from django.conf import settings

class SupabaseStorage(Storage):
    def __init__(self):
        self.project_url = settings.SUPABASE_URL
        self.api_key = settings.SUPABASE_API_KEY
        self.bucket = settings.SUPABASE_BUCKET

    def _get_headers(self):
        return {
            "apikey": self.api_key,
            "Authorization": f"Bearer {self.api_key}",
        }

    def _save(self, name, content):
        upload_url = f"{self.project_url}/storage/v1/object/{self.bucket}/{name}"
        headers = self._get_headers()
        response = requests.post(
            upload_url,
            headers=headers,
            data=content.read(),
        )
        if not response.ok:
            raise Exception(f"Upload failed: {response.text}")
        return name

    def url(self, name):
        return f"{self.project_url}/storage/v1/object/public/{self.bucket}/{name}"

    def exists(self, name):
        return False  # Always upload