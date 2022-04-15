import json

from django.test import TestCase, Client

from lectures.models import Lecture, Category, Schedule, ScheduleLecture, Region, RegionLecture


class LectureDetailViewTest(TestCase):
    def setUp(self):
        Category.objects.create(id=1)
        Schedule.objects.create(id=1, schedule='월')
        Region.objects.create(id=1, region='서울')
        Lecture.objects.create(
            id             = 1,
            create_at      = '2022-01-01 00:00:00',
            updated_at     = '2022-01-01 00:00:00',
            title          = '베인앤컴퍼니 출신의 논리적으로 일하는 법',
            price          = "10000.00",
            category_id    = 1,
            notice         = 'text',
            recommendation = 'text',
            summary        = 'text',
        )
        ScheduleLecture.objects.create(id=1,lecture_id=1,schedule_id=1)
        RegionLecture.objects.create(id=1,lecture_id=1,region_id=1)

    def tearDown(self):
        Category.objects.all().delete()
        Schedule.objects.all().delete()
        Lecture.objects.all().delete()
        ScheduleLecture.objects.all().delete()
        RegionLecture.objects.all().delete()

    def test_LectureDetailView_get_success(self):
        client = Client()

        response = client.get('/lectures/1')
        self.assertEqual(response.json()['message']['title'], '베인앤컴퍼니 출신의 논리적으로 일하는 법')
        self.assertEqual(response.status_code, 200)

    def test_LectureDetailView_DoesNotExist(self):
        client = Client()

        response = client.get('/lectures/2')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {'message': "invalid_lecture"})