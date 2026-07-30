
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

def setup_cloudinary():
    cloudinary.config(
        cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME", "mock_cloud"),
        api_key = os.getenv("CLOUDINARY_API_KEY", "mock_key"),
        api_secret = os.getenv("CLOUDINARY_API_SECRET", "mock_secret"),
        secure = True
    )

def upload_image(file_obj, public_id=None):
    setup_cloudinary()
    try:
        response = cloudinary.uploader.upload(file_obj, public_id=public_id, folder="gvmc_suraksha/shelters")
        return response.get("secure_url")
    except Exception as e:
        # Mock behavior if Cloudinary is not configured during dev
        return f"https://mock-image-url.com/{public_id or '}.jpg"

def delete_image(public_id):
    setup_cloudinary()
    try:
        cloudinary.uploader.destroy(public_id)
    except Exception:
        pass

