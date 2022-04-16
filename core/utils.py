import jwt

from django.conf import settings
from django.http import JsonResponse

from users.models import User

def token_validate(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)

            payload      = jwt.decode(access_token, settings.SECRET_KEY, settings.ALGORITHM)
            request.user = User.objects.get(id=payload['user_id'])

            return func(self, request, *args, **kwargs)

        except jwt.exceptions.DecodeError:
            return JsonResponse({'message': 'invalid_token'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message': 'invalid_user'}, status=400)
        except jwt.exceptions.ExpiredSignatureError:
            return JsonResponse({'message': 'expired_token'}, status=400)
        
    return wrapper