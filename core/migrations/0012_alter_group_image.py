# Generated by Django 4.2.5 on 2023-11-12 02:52

from django.db import migrations, models
import userauths.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_group_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image',
            field=models.ImageField(blank=True, default='cover.jpg', null=True, upload_to=userauths.models.user_directory_path),
        ),
    ]
