# Generated by Django 3.2 on 2021-05-07 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_registration_mark', models.CharField(max_length=100)),
                ('vehicle_make_and_model', models.CharField(max_length=100)),
                ('mileage_in_kilometers', models.IntegerField()),
                ('date_of_last_technical_inspection', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('drivers_licence_number', models.CharField(max_length=10)),
                ('date_of_birth', models.DateField()),
                ('customer_program', models.CharField(choices=[('gold', ' Zlaty program'), ('platinum', 'Platinovy program'), ('ordinary', 'Bezny program')], max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_of_the_hire', models.DateTimeField()),
                ('end_of_the_hire', models.DateTimeField()),
                ('hire_price_in_euros', models.IntegerField()),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.car')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.customer')),
            ],
        ),
    ]
