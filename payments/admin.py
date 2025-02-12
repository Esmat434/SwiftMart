from django.contrib import admin
from .models import Gateway,Payment
# Register your models here.

@admin.register(Gateway)
class GatewayAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_enable']
    list_filter = ['title','is_enable']
    search_fields = ['title']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id','user','package','gateway','price','status','phone_number',"created_time"]
    list_filter = ['status','gateway','package']
    search_fields = ['user__username','phone_number']