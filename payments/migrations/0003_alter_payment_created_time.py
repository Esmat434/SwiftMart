# Generated by Django 5.1.2 on 2025-02-12 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_token_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
