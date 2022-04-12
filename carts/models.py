from django.db import models

# Create your models here.
from core.models import TimeStampedModel


class Like(TimeStampedModel):
    lectures = models.ForeignKey('lectures.Lecture', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'likes'