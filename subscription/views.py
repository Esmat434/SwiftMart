from django.utils import timezone
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import PackageSerializer,SubscriptionSerializer
from .models import Package,Subscription
# Create your views here.

class PackageView(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class SubscriptionListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        subscriptions = Subscription.objects.filter(
            user = request.user,
            expire_time__gt = timezone.now()
        )
        serializer = SubscriptionSerializer(subscriptions,many=True)
        return Response(serializer.data)