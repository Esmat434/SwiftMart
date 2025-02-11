from rest_framework import serializers
from .models import Category,Product,File

class CategorySerialzier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class ProductSerialzier(serializers.ModelSerializer):
    category = CategorySerialzier()
    file_set = FileSerializer(many=True)
    class Meta:
        model = Product
        fields = ['title','description','avatar','category','file_set']
