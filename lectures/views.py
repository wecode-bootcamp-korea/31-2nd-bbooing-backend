from django.db.models import Count

from django.http  import JsonResponse
from django.views import View

from lectures.models import Lecture, LectureImage

class LectureListView(View):
    def get(self, request):
        offset = int(request.GET.get('offset', 0))
        limit  = int(request.GET.get('limit', 12))

        filter_list_set = {
            'category_id' : 'category_id__in',
            'types_id'    : 'typelecture__type__id__in',
            'regions'     : 'regionlecture__region__region__in',
            'schedules'   : 'schedulelecture__schedule__schedule__in'
        }

        filter_set = {
            'title' : 'title__icontains',
        }

        q = {**{filter_list_set[key] : value for key, value in dict(request.GET).items() if filter_list_set.get(key)},
             **{filter_set[key] : value for key, value in request.GET.items() if filter_set.get(key)}}
        
        lectures = Lecture.objects.select_related('category')\
                                  .prefetch_related('regions', 'schedules', 'types','lectureimage_set')\
                                  .annotate(likes_total = Count('like__id'))\
                                  .filter(**q).order_by('-id')[offset : offset + limit]

        result = [{
                'lecture_id': lecture.id,
                'regions'   : [region.region for region in lecture.regions.all()],
                'schedules' : [schedule.schedule for schedule in lecture.schedules.all()],
                'type_names': [type.type for type in lecture.types.all()],
                'category'  : lecture.category.name,
                'title'     : lecture.title,
                'price'     : lecture.price,
                'likes'     : lecture.likes_total,
                'images'    : [image.image_url for image in lecture.lectureimage_set.all()]
        } for lecture in lectures]

        return JsonResponse({'result' : result}, status = 200)

class LectureView(View):
    def get(self, request):
        lectures = Lecture.objects.select_related('category')\
                                  .prefetch_related('regions', 'schedules', 'types','lectureimage_set')\
                                  .annotate(likes_total=Count('like__id'))\
      
        result = [
        {
            'type_ids'  : [type.id for type in lecture.types.all()],
            'type_names': [type.type for type in lecture.types.all()],
            'lecture_id': lecture.id,
            'title'     : lecture.title,
            'category'  : lecture.category.name,
            'regions'   : [region.region for region in lecture.regions.all()],
            'schedules' : [schedule.schedule for schedule in lecture.schedules.all()], 
            'price'     : lecture.price,
            'likes'     : lecture.likes_total,
            'images'    : [image.image_url for image in lecture.lectureimage_set.all()]
        } for lecture in lectures]
        
        return JsonResponse({'total_list' : result}, status = 200)

class LectureDetailView(View):
    def get(self, request, lecture_id):
        try:
            lecture = Lecture.objects\
                             .prefetch_related('schedulelecture_set', 'regionlecture_set', 'review_set', 'typelecture_set', 'review_set__reviewimage_set')\
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
                    'create'       : review.create_at,
                    'review_image' : [reviewimage.image_url for reviewimage in review.reviewimage_set.all()],
                    'review_id'    : review.id
                } for review in lecture.review_set.all()]
            }

            return JsonResponse({'message': results}, status=200)

        except Lecture.DoesNotExist:
            return JsonResponse({'message': "invalid_lecture"}, status=400)