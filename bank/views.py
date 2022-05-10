from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response
from rest_framework import status
from bank.models import Account
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers
from .serializers import AccountSerializer
# Create your views here.


def Home(request):
    return HttpResponse('Home')

@csrf_exempt
@api_view (['POST']) 
def GetAccount(request):
    account_no = request.POST['account_no']
    if account_no =="":
        return Response({'message':"Please Enter account No."},status=status.HTTP_400_BAD_REQUEST)
    account = Account.objects.get(pk=1)
    serializer=AccountSerializer([account],many=True)
    return Response(serializer.data)

def Contact(request):
    return HttpResponse('Contact')

def DefaultAccounts(request):
    firstAccount = Account(name="Wanjiru", account_no=1234, balance=0)
    firstAccount.save()
    secondAccount = Account(name="Linda", account_no=23434, balance=0)
    secondAccount.save()
    thirdAccount = Account(name="Juma", account_no=1234, balance=0)
    thirdAccount.save()

    return Response('test')