from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PackageView,SubscriptionView

router = DefaultRouter()
router.register(r'packages',PackageView,basename="packages")
router.register(r'subscriptions',SubscriptionView,basename="subscriptions")

urlpatterns = [
    path('',include(router.urls))
]