# Generated by Django 3.1.7 on 2021-04-01 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='featured_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]