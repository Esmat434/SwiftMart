import uuid
from django.utils import timezone
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializer import GatewaySerializer,PaymentSerializer
from .models import Gateway,Payment
from subscription.models import Package,Subscription
# Create your views here.

class GatewayView(viewsets.ModelViewSet):
    queryset = Gateway.objects.all()
    serializer_class = GatewaySerializer

class PaymentView(APIView):
    parser_classes = [IsAuthenticated]

    def get(self,request):
        gateway_id = request.query_params.get('gateway')
        package_id = request.query_params.get('package')

        try:
            package = Package.objects.get(id = package_id,is_enable=True)
            gateway = Gateway.objects.get(id = gateway_id,is_enable = True)
        except (Package.DoesNotExist,Gateway.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        payment = Payment.objects.create(
            user = request.user,
            package = package,
            gateway = gateway,
            price = package.price,
            phone_number = request.user.phone_number,
            token = str(uuid.uuid4())
        )
        return Response({'token':payment.token,'callback_url':'https://azizi_bank.com/payments/pay/'})
    
    def post(self,request):
        token = request.data.get('token')
        st = request.data.get('status')

        try:
            payment = Payment.objects.gert(token=token)
        except Payment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if st != 10:
            payment.status = payment.STATUS_CANCELED
            payment.save()
            return Response({'detail':'payment verification faild'},status=status.HTTP_400_BAD_REQUEST)
        r = request.post('bank_verify_url',data = {})
        if r.status_code // 100 !=2:
            payment.status = payment.STATUS_ERROR
            payment.save()
            return Response({'detail':'payment verification faild'},status=status.HTTP_400_BAD_REQUEST)
         
        payment.status = payment.STATUS_PAID
        payment.save()

        Subscription.objects.create(
            user = request.user,
            package = payment.package,
            expire_time = timezone.now() + timezone.timedelta(days=payment.package.duration.days)
        )

        return Response({'detail':"payment verification successfully."},status=status.HTTP_200_OK)