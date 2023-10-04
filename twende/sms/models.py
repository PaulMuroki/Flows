from django.db import models

# Create your models here.
class Sms(models.Model):
    phone_number = models.CharField(max_length=12)
    text = models.CharField(max_length=254)

class MobileMoneyTransaction(models.Model):
    phone_number = models.CharField(max_length=9)
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_created=True, auto_now=True)
    transaction_id = models.CharField(max_length=16, unique=True,db_index=True)
    reference = models.CharField(max_length=100)
    status = models.CharField(choices=[('TF','Failed'), ('TS', 'Success')], max_length=2)

