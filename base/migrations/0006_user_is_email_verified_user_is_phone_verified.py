# Generated by Django 4.1 on 2023-05-28 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_user_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_phone_verified',
            field=models.BooleanField(default=False),
        ),
    ]
