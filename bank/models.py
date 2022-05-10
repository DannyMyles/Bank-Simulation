from django.db import models

# Create your models here.
class Account(models.Model):
    name=models.CharField(max_length =30)
    balance=models.IntegerField()
    account_no=models.IntegerField(null=True)

    def _str_(self):
        return self.name
    

class Transaction(models.Model):
    account=models.IntegerField((""))
    amount=models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type=models.CharField( max_length=50)
    other_details=models.CharField( max_length=50)
    date=models.DateField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.account
    