# Generated by Django 4.1.5 on 2023-02-02 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BackroundRoom',
            new_name='BackroundBlog',
        ),
    ]
