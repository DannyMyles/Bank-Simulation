from .models import Account,Transaction
from rest_framework import serializers

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account 
        fields= ('name', 'balance','account_no')