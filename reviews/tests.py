from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test     import TestCase, Client
from unittest.mock   import patch


class ReviewView(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch('reviews.views.FileHandler.upload')
    def test_review_post_success(self, mocked_aws):
        client = Client()
        access_token = jwt.encode({
            'user_id': 1,
            'exp': datetime.utcnow() + timedelta(days=1)
        }, settings.SECRET_KEY, settings.ALGORITHM)

        headers = {'HTTP_Authorization': access_token}

        image = SimpleUploadedFile(name='car.jpg',
                                   content=open('/Users/gleehave/Desktop/bbooing/DB/data/car.jpg', 'rb').read(),
                                   content_type='image/jpg')
        data = {
            "content"     : "test댓글",
            "review_image": [image]
        }

        mocked_aws.return_value = 'https://bbooingimage.s3.ap-northeast-2.amazonaws.com/car.jpg'

        response = client.post('/reviews/lectures/1', data=data, format='multipart', **headers)