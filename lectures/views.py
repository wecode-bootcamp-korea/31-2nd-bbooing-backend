from django.http  import JsonResponse
from django.views import View

from lectures.models import Lecture, LectureImage

class LectureDetailView(View):
    def get(self, request, lecture_id):
        try:
            lecture = Lecture.objects\
                             .prefetch_related('schedulelecture_set', 'regionlecture_set', 'review_set','typelecture_set')\
                             .get(id=lecture_id)
            images = LectureImage.objects.filter(lecture_id=lecture_id)

            results = {
                'title'         : lecture.title,
                'thumbnail'     : lecture.thumbnail_image_url,
                'price'         : lecture.price,
                'notice'        : lecture.notice,
                'summary'       : lecture.summary,
                'recommendation': lecture.recommendation,
                'types'         : lecture.typelecture_set.get().type.type,
                'schedule'      : lecture.schedulelecture_set.get().schedule.schedule,
                'region'        : lecture.regionlecture_set.get().region.region,
                'images'        : [{'image': image.image_url} for image in images],
                'reviews'       : [{
                    'user'         : review.user.kakao_nickname,
                    'profile_image': review.user.profile_image,
                    'content'      : review.content,
                    'create'       : review.create_at
                } for review in lecture.review_set.all()]
            }

            return JsonResponse({'message': results}, status=200)

        except Lecture.DoesNotExist:
            return JsonResponse({'message': "invalid_lecture"}, status=400)