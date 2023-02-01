# Generated by Django 4.1.5 on 2023-02-01 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_delete_backroundindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='partners/', verbose_name='Логотип партнера')),
                ('url', models.URLField(verbose_name='Ссылка на них')),
            ],
            options={
                'verbose_name': 'Наш партнер',
                'verbose_name_plural': 'Наши  партнеры',
            },
        ),
    ]