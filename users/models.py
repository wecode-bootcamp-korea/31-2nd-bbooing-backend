from django.db import models

from core.models import TimeStampedModel


class User(TimeStampedModel):
    lectures      = models.ManyToManyField('lectures.Lecture', through='LectureUser')
    point         = models.IntegerField(default=1000000)
    kakao_id      = models.BigIntegerField()
    kakao_email   = models.CharField(max_length=100, null=True)
    profile_image = models.CharField(max_length=2000,
                                         default='https://media.istockphoto.com/photos/cute-blue-robot-giving-thumbs-up-3d-picture-id1350820098?b=1&k=20&m=1350820098&s=170667a&w=0&h=8gO4GcPH-wsEZS6PYn2WXbQN3ZPPv98vE6mBl-Ckwr8=')

    class Meta:
        db_table = 'users'

class LectureUser(models.Model):
    lecture = models.ForeignKey('lectures.Lecture', on_delete=models.CASCADE)
    user    = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        db_table = 'lectures_users'
