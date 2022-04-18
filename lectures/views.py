from django.db.models import Q, Count

from django.http  import JsonResponse
from django.views import View

from lectures.models import Lecture, LectureImage

class LectureListView(View):
    def get(self, request):
        category_id = request.GET.getlist('category_id', None)
        types_id    = request.GET.getlist('types_id', None)
        regions     = request.GET.getlist('regions', None)
        schedules   = request.GET.getlist('schedules', None)
        offset      = int(request.GET.get('offset', 0))
        limit       = int(request.GET.get('limit', 12))

        condition = Q()

        if category_id:
            condition &= Q(category_id__in = category_id)

        if types_id:
            condition &= Q(typelecture__type__id__in = types_id)
    
        if regions:
            condition &= Q(regionlecture__region__region__in = regions)

        if schedules:
            condition &= Q(schedulelecture__schedule__schedule__in = schedules)

        lectures = Lecture.objects.select_related('category')\
                                  .prefetch_related('regions', 'schedules', 'types','lectureimage_set','lectureuser_set')\
                                  .filter(condition).order_by('-id')[offset : offset + limit]

        likes = Lecture.objects.values('id').annotate(likes_total = Count('lectureuser__user_id'))
        
        result = [{
            'id'        : lecture.id,
            'regions'   : lecture.regions.get().region,
            'schedules' : lecture.schedules.get().schedule, 
            'types'     : lecture.types.get().id,
            'category'  : lecture.category.name,
            'title'     : lecture.title,
            'price'     : lecture.price,
            'likes'     : likes[lecture.id-1]['likes_total'],
            'images'    : [image.image_url for image in lecture.lectureimage_set.all()]
        } for lecture in lectures]

        return JsonResponse({'result' : result}, status = 200)

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