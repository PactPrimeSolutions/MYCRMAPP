# Generated by Django 5.0.1 on 2024-08-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_businessdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('received_on', models.DateField()),
                ('organization_date', models.DateField()),
                ('assigned_on', models.DateField()),
                ('sl', models.CharField(blank=True, max_length=100)),
                ('batch_type', models.CharField(blank=True, max_length=100)),
                ('order_no', models.CharField(blank=True, max_length=100)),
                ('borrower_name_1', models.CharField(blank=True, max_length=255)),
                ('borrower_name_2', models.CharField(blank=True, max_length=255)),
                ('address', models.TextField(blank=True, max_length=500)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('loan_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(blank=True, max_length=100)),
                ('processor_name', models.CharField(blank=True, max_length=100)),
                ('typing', models.CharField(blank=True, max_length=100)),
                ('completed_on', models.DateField(blank=True, null=True)),
                ('order', models.CharField(blank=True, max_length=100)),
                ('acer', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='BusinessDetail',
        ),
    ]
