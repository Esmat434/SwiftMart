from django.db import models

# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2048,blank=True)
    avatar = models.ImageField(upload_to="images/category",blank=True)
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2048,blank=True)
    is_enable = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to="images/product",blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class File(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="files/product/%Y/%m/%d/")
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)