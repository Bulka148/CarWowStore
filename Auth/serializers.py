
from rest_framework.serializers import ModelSerializer
from Auth.models import *


class User_serializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class Seller_serializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'


class Seller_passport_serializer(ModelSerializer):
    class Meta:
        model = Seller_passport
        fields = '__all__'


