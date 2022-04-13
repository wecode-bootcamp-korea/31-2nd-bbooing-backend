from django.db import models

from core.models import TimeStampedModel


class Review(TimeStampedModel):
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    lecture = models.ForeignKey('lectures.Lecture', on_delete=models.CASCADE)
    content = models.CharField(max_length=3000)

    class Meta:
        db_table = 'reviews'

class ReviewImage(TimeStampedModel):
    review   = models.ForeignKey('Review', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'review_images'