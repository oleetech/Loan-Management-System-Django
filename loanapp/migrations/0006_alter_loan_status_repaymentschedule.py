# Generated by Django 4.0.10 on 2023-10-27 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0005_loan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(choices=[('1', 'Open'), ('2', 'Running'), ('3', 'Closed')], default='1', max_length=20),
        ),
        migrations.CreateModel(
            name='RepaymentSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installment_number', models.PositiveIntegerField()),
                ('due_date', models.DateField()),
                ('amount_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loanapp.loan')),
            ],
        ),
    ]