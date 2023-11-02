# Generated by Django 4.0.10 on 2023-10-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0003_customersdocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('max_loan_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]