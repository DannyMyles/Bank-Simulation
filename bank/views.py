from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response
from rest_framework import status
from bank.models import Account,Transaction
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core import serializers
from .serializers import AccountSerializer,TransactionSerializer
from django import forms

# Create your views here.


def Home(request):
    return render(request, 'home.html', {})

''' getting bank account using the account np '''
@csrf_exempt
@api_view (['POST']) 
def GetAccount(request):
    ''' Capture the account number being posted '''
    account_no = request.POST['account_no']
    ''' validate if the account number field is empty '''  
    if account_no =="":
        return Response({'message':"Please Enter account No."},status=status.HTTP_400_BAD_REQUEST)

    ''' we query the database to retrive the account info and we get the first from the list '''
    account = Account.objects.filter(account_no=account_no)
    if len(account)==0:
        return Response({'message':"Invalid Accout"},status=status.HTTP_400_BAD_REQUEST)
    
    
    ''' we query all the transaction tied to this accont from the transaction table '''
    transactions=Transaction.objects.filter(account__account_no=account_no)
    transaction_data=TransactionSerializer(transactions).data

    ''' serialize the account data to a dictionary'''
    account_data=AccountSerializer(account,many=True).data[0]
    ''' include the transaction data into the account data '''
    account_data["trasactions"] = transaction_data
    
    ''' send the response with the data '''
    return Response(account_data)


@csrf_exempt
@api_view (['POST']) 
def Deposit(request):
    account_no=request.POST['account_no']
    if account_no =="":
        return Response({'message':"Please Enter account No."},status=status.HTTP_400_BAD_REQUEST)

    amount=int(request.POST['amount'])
    if amount =="":
        return Response({'message':"Please Enter Amount."},status=status.HTTP_400_BAD_REQUEST)
    elif amount < 0:
        return Response({'message':"Invalid Amount"},status=status.HTTP_400_BAD_REQUEST)


    account = Account.objects.filter(account_no=account_no)
    if len(account)==0:
        return Response({'message':"Invalid Accout"},status=status.HTTP_400_BAD_REQUEST)

    account = Account.objects.get(pk=account[0].pk)
    transaction=Transaction(id=None, amount=amount,transaction_type="D",account=account,date=datetime.now,other_details="")
    transaction.save()
    print(account)
    new_account_bal= amount+account.balance
    account.balance=new_account_bal
    account.save()
    print(new_account_bal)
    return Response({'message':f'Ammount Deposited to the Account, your new balance is {new_account_bal}'})


@csrf_exempt
@api_view (['POST'])
def Withdrawal(request):
    
    account_no=request.POST['account_no']
    if account_no =="":
        return Response({'message':"Please Enter account No."},status=status.HTTP_400_BAD_REQUEST)

    amount=int(request.POST['amount'])
    if amount =="":
        return Response({'message':"Please Enter Amount."},status=status.HTTP_400_BAD_REQUEST)
    elif amount < 0:
        return Response({'message':"Invalid Amount"},status=status.HTTP_400_BAD_REQUEST)


    account = Account.objects.filter(account_no=account_no)
    if len(account)==0:
        return Response({'message':"Invalid Accout"},status=status.HTTP_400_BAD_REQUEST)

    account = Account.objects.get(pk=account[0].pk)
    transaction=Transaction(id=None, amount=amount,transaction_type="W",account=account,date=datetime.now(),other_details="")
    transaction.save()
    print(account)
    new_account_bal=account.balance-amount
    account.balance=new_account_bal
    account.save()
    print(new_account_bal)
    return Response({'message':f'Withdrew from Account, your new balance is {new_account_bal}'})


@csrf_exempt
@api_view (['POST'])
def Transfer(request):
    account_no=request.POST['account_from']
    if account_no =="":
        return Response({'message':"Please Enter account No."},status=status.HTTP_400_BAD_REQUEST)

    amount=int(request.POST['amount'])
    if amount =="":
        return Response({'message':"Please Enter Amount To Transfer."},status=status.HTTP_400_BAD_REQUEST)
    elif amount < 0:
        return Response({'message':"Invalid Amount"},status=status.HTTP_400_BAD_REQUEST)

    account = Account.objects.filter(account_no=account_no)
    if len(account)==0:
        return Response({'message':"Invalid Accout"},status=status.HTTP_400_BAD_REQUEST)

    account = Account.objects.get(pk=account[0].id)

    transfer_to = request.POST['account_to']
    if transfer_to =="":
        return Response({'message':"Please Enter receiving account No."},status=status.HTTP_400_BAD_REQUEST)
        
    receiving_account = Account.objects.filter(account_no=transfer_to)
    if len(receiving_account)==0:
        return Response({'message':"The receiving account is Invalid"},status=status.HTTP_400_BAD_REQUEST)
    receiving_account = Account.objects.get(pk=receiving_account[0].id)

    transaction = Transaction(id=None, account=account, amount=amount, transaction_type="T", date=datetime.now(),other_details=transfer_to )
    transaction.save()

    new_debited_bal=account.balance+amount
    account.balance=new_debited_bal
    account.save()

    new_credited_bal=receiving_account.balance-amount
    receiving_account.balance=new_credited_bal
    receiving_account.save()

    return Response({'message':"Transfer successful"})
    
@csrf_exempt
@api_view (['POST']) 
def ImportTransactions(request):
    print(request.FILES)
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
        return Response("Good post")

    return Response("Reupload file")

def Contact(request):
    return HttpResponse('Contact')

def DefaultAccounts(request):
    firstAccount = Account(name="Wanjiru", account_no=1234, balance=0)
    firstAccount.save()
    secondAccount = Account(name="Linda", account_no=23434, balance=0)
    secondAccount.save()
    thirdAccount = Account(name="Juma", account_no=1233, balance=0)
    thirdAccount.save()

    return Response('test')


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()