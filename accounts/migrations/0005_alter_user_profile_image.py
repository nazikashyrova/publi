# Generated by Django 4.2.1 on 2023-06-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_friendshiprequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(upload_to='profile_images/'),
        ),
    ]
