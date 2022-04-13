from django.db import models

from core.models import TimeStampedModel


class Lecture(TimeStampedModel):
    regions             = models.ManyToManyField('Region', through='RegionLecture')
    schedules           = models.ManyToManyField('Schedule', through='ScheduleLecture')
    types               = models.ManyToManyField('Type', through='TypeLecture')
    category            = models.ForeignKey('Category', on_delete=models.CASCADE)
    title               = models.CharField(max_length=100)
    price               = models.DecimalField(max_digits=9, decimal_places=2)
    notice         = models.CharField(max_length=3000, default='text')
    summary        = models.CharField(max_length=3000, default='text')
    recommendation = models.CharField(max_length=3000, default='text')
    thumbnail_image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'lectures'

class LectureImage(TimeStampedModel):
    lecture   = models.ForeignKey('Lecture', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=2000)
    sequence  = models.PositiveIntegerField()

    class Meta:
        db_table = 'lecture_images'

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'categories'

class Region(models.Model):
    region = models.CharField(max_length=100)

    class Meta:
        db_table = 'regions'

class Schedule(models.Model):
    schedule = models.CharField(max_length=100)

    class Meta:
        db_table = 'schedules'

class Type(models.Model):
    type = models.CharField(max_length=100)

    class Meta:
        db_table = 'types'

class RegionLecture(models.Model):
    region  = models.ForeignKey('Region', on_delete=models.CASCADE)
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE)

    class Meta:
        db_table = 'regions_lectures'

class ScheduleLecture(models.Model):
    schedule = models.ForeignKey('Schedule', on_delete=models.CASCADE)
    lecture  = models.ForeignKey('Lecture', on_delete=models.CASCADE)

    class Meta:
        db_table = 'schedules_lectures'

class TypeLecture(models.Model):
    type    = models.ForeignKey('Type', on_delete=models.CASCADE)
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE)

    class Meta:
        db_table = 'types_lectures'
