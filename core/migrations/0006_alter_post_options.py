# Generated by Django 4.2.5 on 2023-11-03 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_group_page_pagepost_grouppost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Post'},
        ),
    ]
