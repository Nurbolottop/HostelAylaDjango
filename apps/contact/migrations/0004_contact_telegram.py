# Generated by Django 4.1.5 on 2023-01-30 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_contact_telegram'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='telegram',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на Telegram'),
        ),
    ]