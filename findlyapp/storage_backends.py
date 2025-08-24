import requests
from django.core.files.storage import Storage
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

class SupabaseStorage(Storage):
    def __init__(self):
        self.project_url = getattr(settings, "SUPABASE_URL", None)
        self.api_key = getattr(settings, "SUPABASE_API_KEY", None)
        self.bucket = getattr(settings, "SUPABASE_BUCKET", None)

        if not all([self.project_url, self.api_key, self.bucket]):
            raise ImproperlyConfigured("SupabaseStorage requires SUPABASE_URL, SUPABASE_API_KEY, and SUPABASE_BUCKET to be set in settings.")

    def _get_headers(self):
        return {
            "apikey": self.api_key,
            "Authorization": f"Bearer {self.api_key}",
            # Optionally, you can specify content-type here if you want
        }

    def _save(self, name, content):
        print(f"🔄 Uploading '{name}' to Supabase...")
        upload_url = f"{self.project_url}/storage/v1/object/{self.bucket}/{name}"
        headers = self._get_headers()
        response = requests.put(
            upload_url,
            headers=headers,
            data=content.read(),
        )
        if not response.ok:
            raise Exception(f"Upload failed: {response.status_code} - {response.text}")
        return name

    def url(self, name):
        return f"{self.project_url}/storage/v1/object/public/{self.bucket}/{name}"

    def exists(self, name):
        # Always return False so Django attempts to upload the file every time
        return False

    def size(self, name):
        # Optional: Implement this if you want Django to report file sizes
        return None

    def delete(self, name):
        # Optional: Add code here if you want to support deleting files from Supabase Storage
        pass
