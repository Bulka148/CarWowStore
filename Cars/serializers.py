
from rest_framework.serializers import ModelSerializer

from Auth.models import Seller
from Auth.serializers import Seller_serializer
from Cars.models import *


class Firm_serializer(ModelSerializer):
    class Meta:
        model = Firm
        fields = '__all__'


class Car_passport_serializer(ModelSerializer):
    class Meta:
        model = Car_passport
        fields = '__all__'


class Car_serializer(ModelSerializer):
    model = Firm_serializer()
    passport = Car_passport_serializer()
    seller = Seller_serializer()

    class Meta:
        model = Car
        fields = '__all__'

    def create(self, request):
        if not Seller.objects.filter(user=request['seller']['user']):
            Seller(user=request['seller']['user'], phone=request['seller']['phone']).save()
        Car(model=Firm.objects.get(name=request['model']['name']), price=request['price'],
            city=request['city'], seller=Seller.objects.get(user=request['seller']['user'])).save()

        return request


class Car_shop_serializer(ModelSerializer):
    firm = Firm_serializer()

    class Meta:
        model = Car_shop
        fields = '__all__'


class Sale_serializer(ModelSerializer):

    class Meta:
        model = Sale
        fields = '__all__'
