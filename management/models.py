from django.db import models
from django.contrib.auth.models import User

class Consumer(models.Model):
    name = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User, related_name='consumer', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    consumer = models.ForeignKey(Consumer, on_delete=models.SET_NULL,related_name='order', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, null=True)
    quantity = models.IntegerField(default=1)


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    consumer = models.ForeignKey(Consumer,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()


    def __str__(self):
        return self.consumer.name



