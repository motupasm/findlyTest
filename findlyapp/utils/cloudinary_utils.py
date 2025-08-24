import cloudinary
import cloudinary.uploader
import cloudinary.api
from django.conf import settings

# Configure Cloudinary with your credentials from settings
cloudinary.config(
    cloud_name = settings.CLOUDINARY_CLOUD_NAME,
    api_key = settings.CLOUDINARY_API_KEY,
    api_secret = settings.CLOUDINARY_API_SECRET,
)

def upload_to_cloudinary(file):
    result = cloudinary.uploader.upload(file)
    return result.get("secure_url")
