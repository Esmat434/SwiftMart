from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PackageView,SubscriptionListView

router = DefaultRouter()
router.register(r'packages',PackageView,basename="packages")

urlpatterns = [
    path('subscriptions/',SubscriptionListView.as_view()),
    path('',include(router.urls))
]