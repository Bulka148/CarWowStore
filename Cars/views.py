import stripe
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from CarWowStore import settings
from CarWowStore.settings import BASE_URL, BASE_FRONT_URL
from Cars.serializers import *


class CarAPIViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = Car_serializer
    permission_classes = [permissions.AllowAny]


class SaleAPIViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = Sale_serializer
    permission_classes = [permissions.IsAuthenticated]


class FirmAPIViewSet(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = Firm_serializer
    permission_classes = [permissions.AllowAny]


class SuccessView(View):
    def get(self, request):
        car = Car.objects.get(id=request.GET.get('car_id', 0))
        user = User.objects.get(id=request.GET.get('user_id', 0))
        Sale(car=car, buyer=user).save()
        return redirect(BASE_FRONT_URL + f'successBuy')


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = BASE_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + f'success/?car_id={request.GET.get("car_id")}&'
                                         f'user_id={request.GET.get("user_id")}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price': 'price_1N9op1DMsElZx2zYVwIr5NS8',
                        'quantity': 1,
                    }
                ]
            )
            return redirect(checkout_session['url'])
        except Exception as e:
            return JsonResponse({'error': str(e)})


class CancelledView(View):
    def get(self, request):
        return redirect(BASE_FRONT_URL + 'cancelledBuy')

