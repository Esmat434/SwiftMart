from django.contrib import admin
from .models import Package,Subscription
# Register your models here.

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_enable','price','stock','duration','created_time']
    list_filter = ['is_enable','title']
    search_fields = ['title']

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id','user','package','created_time']
    list_filter = ['user','package']
    search_fields = ['package']
    