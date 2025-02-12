from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Package(models.Model):
    title = models.CharField(max_length=200,db_index=True)
    description = models.CharField(max_length=2048,blank=True)
    avatar = models.ImageField(upload_to="images/subscription/%Y/%m/%d/")
    is_enable = models.BooleanField(default=True)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    duration = models.DurationField(blank=True,null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    package = models.ForeignKey(Package,on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    expire_time = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.user.username