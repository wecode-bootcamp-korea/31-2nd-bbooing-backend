from django.db import models

from core.models import TimeStampedModel


class Order(TimeStampedModel):
    payment = models.ForeignKey('PaymentType', on_delete=models.CASCADE)
    lecture = models.ForeignKey('lectures.Lecture', on_delete=models.CASCADE)
    user    = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name    = models.CharField(max_length=200)
    status  = models.CharField(max_length=100)

    class Meta:
        db_table = 'orders'

class PaymentType(models.Model):
    payment = models.CharField(max_length=200)

    class Meta:
        db_table = 'payment_type'