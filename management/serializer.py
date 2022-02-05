from rest_framework import serializers
from  .models import *


class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Consumer
        fields= ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields= ('__all__')

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields= '__all__'


