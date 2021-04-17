# Generated by Django 3.2 on 2021-04-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_of_the_hire', models.DateTimeField()),
                ('end_of_the_hire', models.DateTimeField()),
                ('hire_price_in_euros', models.IntegerField()),
            ],
        ),
    ]