import requests, jwt

from datetime import datetime, timedelta

from django.http  import JsonResponse
from django.conf  import settings
from django.views import View

from .models import *

class KakoAPI:
    def __init__(self, access_token):
        self.access_token = access_token
        self.user_url     = 'https://kapi.kakao.com//v2/user/me'

    def get_kakao_user(self):
        try:
            headers  = {'Authorization' : f'Bearer {self.access_token}'}
            response = requests.get(self.user_url, headers = headers, timeout=2.5)

            if not response.code == 200: 
                return JsonResponse({'message':'INVALID_USER'}, status = 401)

            return response.json() 
        except requests.exceptions.Timeout:
                return JsonResponse({'message' : 'TIME_OUT_ERROR'}, status = 408)

class KakaoLoginView(View):
    def post(self, request):
        try: 
            kakao_token = request.headers.get('Authorization')
            kakao_user  = KakoAPI(kakao_token)

            kakao_id       = kakao_user['id']
            kakao_nickname = kakao_user['properties']['nickname']
            kakao_email    = kakao_user['kakao_account']['email']
            profile_image  = kakao_user['properties']['profile_image']

            user, is_created = User.objects.get_or_create(
                kakao_id = kakao_id,
                defaults = {'kakao_nickname' : kakao_nickname, 'kakao_email' : kakao_email, 'profile_image' : profile_image}
            )
            
            data = {
                'access_token'   : jwt.encode({'user_id' : user.id, 'exp' : datetime.utcnow() + timedelta(days=1)}, settings.SECRET_KEY, algorithm = settings.ALGORITHM),
                'kakao_nickname' : kakao_nickname,
                'profile_image'  : profile_image
            }
            
            status_code  = 201 if is_created else 200
            
            return JsonResponse({'access_token' : data}, status = status_code)

        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)