# Generated by Django 3.2 on 2022-05-09 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_no',
            field=models.IntegerField(null=True),
        ),
    ]
