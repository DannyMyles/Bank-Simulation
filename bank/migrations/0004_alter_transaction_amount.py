# Generated by Django 3.2 on 2022-05-10 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20220510_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.IntegerField(verbose_name=0),
        ),
    ]
