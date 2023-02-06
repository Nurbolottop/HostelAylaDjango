# Generated by Django 4.1.5 on 2023-02-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_remove_about_image1_remove_about_image2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_history', verbose_name='Фотография')),
                ('years', models.CharField(max_length=244, verbose_name='Год')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Наша история',
                'verbose_name_plural': 'Наша история',
            },
        ),
    ]