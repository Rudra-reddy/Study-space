# Generated by Django 4.0 on 2022-06-29 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='displaypicture',
            field=models.ImageField(default='dp.jpg', null=True, upload_to=''),
        ),
    ]
