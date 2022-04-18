from django.test   import TestCase, Client
from unittest.mock import patch 

from users.models import User
from users.views  import KakaoAPI

class KakaoLogInTest(TestCase): 
    def setUp(self):
        User.objects.create(
            id             = 1,
            create_at      = '2022-01-01 00:00:00',
            updated_at     = '2022-01-01 00:00:00',
            kakao_id       = 123456,
            kakao_email    = 'boni@gmail.com',
            kakao_nickname = '구보니보니',
            profile_image  = 'https://media.istockphoto.com/photos/cute-blue-robot-giving-thumbs-up-3d-picture-id1350820098?b=1&k=20&m=1350820098&s=170667a&w=0&h=8gO4GcPH-wsEZS6PYn2WXbQN3ZPPv98vE6mBl-Ckwr8='
        )

    def tearDown(self):
        User.objects.all().delete()

    @patch.object(KakaoAPI, 'get_kakao_user')
    def test_success_kakao_login_new_user_create(self, mocked_request):
        client = Client()

        mocked_request.return_value = {
            'id' : 987654, 
            'kakao_account' : {
                'email' : 'bbooing@gmail.com'
            },
            'properties' : {
                'nickname'      : 'bbooing',
                'profile_image' : 'https://media.istockphoto.com/photos/cute-blue-robot-giving-thumbs-up-3d-picture-id1350820098?b=1&k=20&m=1350820098&s=170667a&w=0&h=8gO4GcPH-wsEZS6PYn2WXbQN3ZPPv98vE6mBl-Ckwr8='
            }
        }
        response = client.post('/users/kakao-login')
        
        self.assertEqual(response.status_code, 201)

    @patch.object(KakaoAPI, 'get_kakao_user')
    def test_success_kakao_login_existed_user(self, mocked_request):
        client = Client()

        mocked_request.return_value = {
            'id' : 123456,
            'kakao_account' : {
                'email' : 'boni@gmail.com'
            },
            'properties' : {
                'nickname'      : '구보니보니',
                'profile_image' : 'https://media.istockphoto.com/photos/cute-blue-robot-giving-thumbs-up-3d-picture-id1350820098?b=1&k=20&m=1350820098&s=170667a&w=0&h=8gO4GcPH-wsEZS6PYn2WXbQN3ZPPv98vE6mBl-Ckwr8='
            }
        }
        response = client.post('/users/kakao-login')
        
        self.assertEqual(response.status_code, 200)
