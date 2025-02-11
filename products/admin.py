from django.contrib import admin
from .models import  Category,Product,File
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','parent','title','is_enable','created_time']
    list_filter = ['is_enable','parent']
    search_fields = ['title']

class FileAdmin(admin.StackedInline):
    model = File
    fields = ['id','title','file']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','is_enable','created_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    inlines = (FileAdmin,)