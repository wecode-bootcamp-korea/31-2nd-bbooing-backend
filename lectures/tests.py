import json

from django.test import TestCase, Client

from lectures.models import Category, RegionLecture, ScheduleLecture, Type, Region, Schedule, Lecture, LectureImage, TypeLecture

class LectureListViewTest(TestCase):
    def setUp(self):
        Category.objects.create(id = 1)
        Type.objects.create(id = 1, type = '오프라인')
        Type.objects.create(id = 2, type = 'VOD')
        Region.objects.create(id = 1, region = '서울')
        Schedule.objects.create(id = 1, schedule = '월요일')
        Lecture.objects.create(
            id                  = 1,
            create_at           = '2022-01-01 00:00:00',
            updated_at          = '2022-01-01 00:00:00',
            category_id         = 1,
            title               = '베인앤컴퍼니 출신의 논리적으로 일하는 법',
            price               = '10000.00',
            notice              = 'text',
            summary             = 'text',
            recommendation      = 'text',
            thumbnail_image_url = 'https://bbooing.s3.ap-northeast-2.amazonaws.com/photo-1448523183439-d2ac62aca997.avif'
        )

        Lecture.objects.create(
            id                  = 2,
            create_at           = '2022-01-01 00:00:00',
            updated_at          = '2022-01-01 00:00:00',
            category_id         = 1,
            title               = '기초부터 배우는 초단간 5분 드로잉',
            price               = '50000.00',
            notice              = 'text',
            summary             = 'text',
            recommendation      = 'text',
            thumbnail_image_url = 'https://bbooing.s3.ap-northeast-2.amazonaws.com/photo-1448523183439-d2ac62aca997.avif'
        )

        LectureImage.objects.create(
            id         = 1, 
            lecture_id = 1, 
            image_url  = 'https://bbooing.s3.ap-northeast-2.amazonaws.com/photo-1448523183439-d2ac62aca997.avif',
            sequence   = 1
        )

        LectureImage.objects.create(
            id         = 2, 
            lecture_id = 2, 
            image_url  = 'https://bbooing.s3.ap-northeast-2.amazonaws.com/photo-1448523183439-d2ac62aca997.avif',
            sequence   = 1
        )

        RegionLecture.objects.create(id = 1, region_id = 1, lecture_id = 1)
        RegionLecture.objects.create(id = 2, region_id = 1, lecture_id = 2)
        ScheduleLecture.objects.create(id = 1, schedule_id = 1, lecture_id = 1)
        ScheduleLecture.objects.create(id = 2, schedule_id = 1, lecture_id = 2)
        TypeLecture.objects.create(id = 1, type_id = 1, lecture_id = 1)
        TypeLecture.objects.create(id = 2, type_id = 2, lecture_id = 2)

    def tearDown(self):
        Category.objects.all().delete()
        Type.objects.all().delete()
        Region.objects.all().delete()
        Schedule.objects.all().delete()
        Lecture.objects.all().delete()
        LectureImage.objects.all().delete()
        RegionLecture.objects.all().delete()
        ScheduleLecture.objects.all().delete()
        TypeLecture.objects.all().delete()

    def test_success_lecture_list_view_get(self):
        client = Client() 
        
        response = client.get('/lectures?category_id=1&types_id=2')
        self.assertEqual(response.json()['result'][0]['title'], '기초부터 배우는 초단간 5분 드로잉')
        self.assertEqual(response.status_code, 200)

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