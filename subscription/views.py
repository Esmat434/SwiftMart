from rest_framework import viewsets
from .serializer import PackageSerializer,SubscriptionSerializer
from .models import Package,Subscription
# Create your views here.

class PackageView(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class SubscriptionView(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer