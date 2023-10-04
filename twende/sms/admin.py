from django.contrib import admin
from sms.models import Sms, MobileMoneyTransaction

@admin.register(Sms)
class SmsAdmin(admin.ModelAdmin):
    pass

@admin.register(MobileMoneyTransaction)
class MobileMoneyTransactionAdmin(admin.ModelAdmin):
    pass
