import jwt
from django.conf import settings
from core.models import User 

def get_user_from_token(token):
    try:
        decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded['user_id']  
        user = User.objects.get(id=user_id)
        return {
            "name": user.name,
            "email": user.email,
            "phone_number": user.phone_number,
            "address": user.address,
            "city": user.city,
            "country": user.country,
        }
    except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
        return None
