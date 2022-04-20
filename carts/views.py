from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.views import View

from carts.models import Like
from core.utils import validate_token

class CartView(View):
    @validate_token
    def post(self, request, lectures_id):
        try:
            user        = request.user

            like, is_created = Like.objects.get_or_create(
                user_id     = user.id,
                lectures_id = lectures_id,
            )

            return JsonResponse({'message': "success"}, status=201)

        except KeyError:
            return JsonResponse({'message': "key_error"}, status=400)

    @validate_token
    def get(self, request):
        user  = request.user
        likes = Like.objects.filter(user_id=user.id)

        results = [{
            "like_id"       : like.id,
            "thumbnail_url" : like.lectures.thumbnail_image_url,
            "name"          : like.lectures.title,
            "price"         : like.lectures.price,
            "summary"       : like.lectures.summary
        } for like in likes]

        return JsonResponse({'results': results}, status=200)

    @validate_token
    def delete(self, request, lectures_id):
            user_id  = request.user.id

            if not Like.objects.filter(Q(id=lectures_id) & Q(user_id=user_id)).exists():
                return JsonResponse({"message": 'empty'}, status=400)

            Like.objects.filter(lectures_id=lectures_id, user=user_id).delete()

            return HttpResponse(status=204)