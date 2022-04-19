import json
from datetime import datetime, timedelta

import jwt
from django.conf import settings
from django.test import TestCase, Client

from lectures.models import Lecture, Category, Schedule, ScheduleLecture, Region, RegionLecture
from carts.models import Like
from users.models import User


class CartViewTest(TestCase):
    def setUp(self):
        User.objects.create(id=1, kakao_id=1, kakao_email='aaa@naver.com', kakao_nickname='admin1')
        User.objects.create(id=2, kakao_id=2, kakao_email='bbb@naver.com', kakao_nickname='admin2')
        Category.objects.create(id=1)
        Schedule.objects.create(id=1, schedule='월')
        Region.objects.create(id=1, region='서울')
        Lecture.objects.create(
            id             = 1,
            title          = '베인앤컴퍼니 출신의 논리적으로 일하는 법',
            price          = "10000.00",
            category_id    = 1,
            notice         = 'notice',
            recommendation = 'recommendation',
            summary        = 'summary',
        )
        ScheduleLecture.objects.create(id=1, lecture_id=1, schedule_id=1)
        RegionLecture.objects.create(id=1, lecture_id=1, region_id=1)
        Like.objects.create(id=1, lectures_id=1, user_id=1)

    def tearDown(self):
        Like.objects.all().delete()
        Category.objects.all().delete()
        Schedule.objects.all().delete()
        Region.objects.all().delete()
        Lecture.objects.all().delete()
        ScheduleLecture.objects.all().delete()
        RegionLecture.objects.all().delete()
        Like.objects.all().delete()

    def test_cart_get_success(self):
        client       = Client()
        access_token = jwt.encode({
            'user_id': 1,
            'exp'    : datetime.utcnow() + timedelta(days=1)
        }, settings.SECRET_KEY, settings.ALGORITHM)
        headers      = {'HTTP_Authorization': access_token}

        response = client.get('/carts/like', **headers)

        self.assertEqual(response.json(), {
            'results': [{
                'like_id': 1,
                'thumbnail_url': '',
                'name': '베인앤컴퍼니 출신의 논리적으로 일하는 법',
                'price': "10000.00",
                'summary': 'summary'
            }]
        })
        self.assertEqual(response.status_code, 200)

    def test_cart_post_like_already_exists_success(self):
        client       = Client()
        access_token = jwt.encode({
            'user_id': 1,
            'exp': datetime.utcnow() + timedelta(days=1)
        }, settings.SECRET_KEY, settings.ALGORITHM)

        headers      = {'HTTP_Authorization': access_token}

        response = client.post('/carts/like/1', content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message': "success"})

    def test_cart_post_like_success(self):
        client       = Client()
        access_token = jwt.encode({
            'user_id': 2,
            'exp': datetime.utcnow() + timedelta(days=1)
        }, settings.SECRET_KEY, settings.ALGORITHM)

        headers      = {'HTTP_Authorization': access_token}

        response = client.post('/carts/like/1', content_type='application/json', **headers)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'message': "success"})

    def test_cart_post_like_delete_success(self):
        client = Client()
        access_token = jwt.encode({
            'user_id': 1,
            'exp': datetime.utcnow() + timedelta(days=1)
        }, settings.SECRET_KEY, settings.ALGORITHM)

        headers = {'HTTP_Authorization': access_token}

        response = client.delete('/carts/like/1', content_type='application/json', **headers)

        self.assertEqual(response.status_code, 204)







