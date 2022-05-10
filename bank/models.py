from django.db import models

# Create your models here.
class Account(models.Model):
    name=models.CharField(max_length =30)
    balance=models.IntegerField()
    account_no=models.IntegerField(null=True)

    def _str_(self):
        return self.name
    

class Transaction(models.Model):
    # account=models.IntegerField(("")
    amount=models.IntegerField(default=0)
    transaction_type=models.CharField(max_length=50, null=True)
    other_details=models.CharField( max_length=50,null=True)
    date=models.DateField(auto_now=True)
    account=models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.account