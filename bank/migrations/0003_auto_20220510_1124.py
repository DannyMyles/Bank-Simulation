# Generated by Django 3.2 on 2022-05-10 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_account_account_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(),
        ),
    ]
