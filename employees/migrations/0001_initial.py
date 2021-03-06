# Generated by Django 3.1.7 on 2021-04-01 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(help_text='Enter the Name of the Employee.', max_length=100)),
                ('position', models.CharField(help_text='The position held by the Employee.', max_length=50, null=True)),
                ('phone_number', models.CharField(help_text="Enter the Employee's Phone Number.", max_length=25)),
                ('email', models.CharField(help_text="Enter the Employee's Email Address.", max_length=50, unique=True)),
            ],
        ),
    ]
