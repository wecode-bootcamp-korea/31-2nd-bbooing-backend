from django.db      import transaction
from django.http    import JsonResponse
from django.views   import View

from core.s3        import S3_Client, FileHandler
from core.utils     import validate_token
from reviews.models import Review, ReviewImage

from my_settings    import accessKey, secretKey, bucket_name, region, prefix

s3client = S3_Client(accessKey, secretKey, bucket_name, region)
 
class ReviewView(View):
    @validate_token
    def post(self, request, lecture_id):
        try:

            user         = request.user

            content      = request.POST['content']

            review_image = request.FILES['review_image']


            s3_controller = FileHandler(s3client)

            with transaction.atomic():
                enroll = Review.objects.create(user_id=user.id,
                                               lecture_id=lecture_id,
                                               content=content)

            review_image_url = s3_controller.upload(directory=prefix, file=review_image)

            Review.objects.get(id=enroll.id, lecture_id=lecture_id)\
                          .reviewimage_set\
                          .create(image_url=review_image_url)

            return JsonResponse({'message': 'success'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'invalid_key'}, status=400)
        except transaction.TransactionManagementError:
            return JsonResponse({'message': 'TransactionManagementError'}, status=400)

    @validate_token
    def delete(self, request, review_id):
        try:
            user = request.user
            image_url = ReviewImage.objects.get(review_id=review_id).image_url
            image_name = image_url[image_url.find('lecture'):]

            s3_controller = FileHandler(s3client)
            s3_controller.delete(bucket_name=bucket_name, file_name=image_name)

            Review.objects.get(id=review_id, user_id=user.id).delete()

            return JsonResponse({'message': 'success'}, status=200)

        except Review.DoesNotExist():
            return JsonResponse({'message': 'DoesNotExist'}, status=400) 