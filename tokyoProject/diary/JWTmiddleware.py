import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        authorization_header = request.headers.get('Authorization')
        
        if authorization_header:
            token = authorization_header.split(' ')[1]
            try:
                payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
                user_id = payload['user_id']
                user = get_user_model().objects.get(pk=user_id)
                request.user = user
            except jwt.ExpiredSignatureError:
                return JsonResponse({'error': 'Token expired'}, status=401)
            except jwt.InvalidTokenError:
                return JsonResponse({'error': 'Invalid token'}, status=401)
            except get_user_model().DoesNotExist:
                return JsonResponse({'error': 'User does not exist'}, status=401)

        response = self.get_response(request)
        return response
