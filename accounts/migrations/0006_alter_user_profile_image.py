# Generated by Django 4.2.1 on 2023-06-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='default.jpg', upload_to='profile_images/'),
        ),
    ]