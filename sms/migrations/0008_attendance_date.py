# Generated by Django 2.2.4 on 2019-09-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0007_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
