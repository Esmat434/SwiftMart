from django.db import models
from django.contrib.auth.models import User
from subscription.models import Package
# Create your models here.

class Gateway(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='images/payments/%Y/%m/%d/')
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Payment(models.Model):
    STATUS_VOID = 0
    STATUS_PAID = 10
    STATUS_ERROR = 20
    STATUS_CANCELED = 30
    STATU_REFUNDED = 31

    STATUS_CHOICES = (
        (STATUS_VOID,'void'),
        (STATUS_PAID,'paid'),
        (STATUS_ERROR,'error'),
        (STATUS_CANCELED,'User Canceled'),
        (STATU_REFUNDED,'Refunded')
    )

    STATUS_TRANSLATION = {
        STATUS_VOID:"Payment could not be processed.",
        STATUS_PAID:"Payment successful.",
        STATUS_ERROR:"Payment has encountered an error.",
        STATUS_CANCELED:"Payment canceled by user.",
        STATU_REFUNDED:"This payment has been refunded."
    }

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='%(class)s')
    package = models.ForeignKey(Package,on_delete=models.CASCADE,related_name='%(class)s')
    gateway = models.ForeignKey(Gateway,on_delete=models.CASCADE,related_name='%(class)s')
    price = models.PositiveIntegerField(default=0)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES,default=STATUS_VOID)
    device_uuid = models.CharField(max_length=40,blank=True)
    token = models.CharField(max_length=100)
    phone_number = models.BigIntegerField()
    consumed_code = models.PositiveIntegerField(null=True,db_index=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)