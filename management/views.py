from django.shortcuts import render


from django.shortcuts import render
from .models import *
from management.serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CreateConsumer(APIView):
    def post(self,request):
        serializer = ConsumerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Consumer.objects.get(id=id)
            serializer = ConsumerSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Consumer.objects.all()
        serializer = ConsumerSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class CreateOrder(APIView):
    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Order.objects.get(id=id)
            serializer = OrderSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Order.objects.all()
        serializer = OrderSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class CreatePayment(APIView):
    def post(self,request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Payment.objects.get(id=id)
            serializer = PaymentSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Payment.objects.all()
        serializer = PaymentSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


def order_view(request):
    if request.user.is_authenticated:
        user=request.user.consumer
        orderlist=Order.objects.filter(consumer=user)
        ordeder_products=[p for p in Order.objects.all() if request.user.consumer== user]
        amount = 0.0
        total_amount=0.0
        consumer= user.name
        order_num = len(orderlist)
        for p in ordeder_products:
            amount=p.quantity * p.product.price
            total_amount += amount
        return render(request,'order.html',{'total_amount':total_amount,'consumer':consumer,'total_num_of_order':order_num})

