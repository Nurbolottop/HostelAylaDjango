# Generated by Django 4.1.5 on 2023-01-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='location',
        ),
        migrations.AddField(
            model_name='room',
            name='clean',
            field=models.CharField(default=1, max_length=255, verbose_name='Оценка чистоты от 1 до 5'),
            preserve_default=False,
        ),
    ]
