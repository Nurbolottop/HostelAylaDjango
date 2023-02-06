# Generated by Django 4.1.5 on 2023-02-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_backroundcontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя!')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Последная Связь ',
                'verbose_name_plural': 'Последние Связи ',
                'ordering': ('id',),
            },
        ),
    ]