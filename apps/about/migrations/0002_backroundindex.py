# Generated by Django 4.1.5 on 2023-01-30 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackroundIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='backround/', verbose_name='Задний фон')),
            ],
            options={
                'verbose_name': 'Задний фон страницы <<О нас>>',
                'verbose_name_plural': 'Задний фон страницы <<О нас>>',
            },
        ),
    ]
