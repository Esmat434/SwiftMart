from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import GatewayView,PaymentView

router = DefaultRouter()

router.register(r'gateways',GatewayView,basename='gateways')

urlpatterns = [
    path('pay/',PaymentView.as_view()),
    path('',include(router.urls))
]