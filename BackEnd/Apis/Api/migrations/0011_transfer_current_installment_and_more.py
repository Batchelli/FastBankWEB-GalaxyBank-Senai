# Generated by Django 4.2.7 on 2023-12-05 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0010_customuser_monthly_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='current_installment',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='transfer',
            name='total_installments',
            field=models.IntegerField(default=1),
        ),
    ]
