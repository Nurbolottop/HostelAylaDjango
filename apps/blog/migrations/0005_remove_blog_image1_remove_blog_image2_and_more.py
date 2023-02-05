# Generated by Django 4.1.5 on 2023-02-05 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='image5',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='about', verbose_name='Фотография блога'),
        ),
        migrations.CreateModel(
            name='ImageBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='about', verbose_name='Фотография блога')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_room', to='blog.blog', verbose_name='Выберите блог')),
            ],
            options={
                'verbose_name': 'Добавить фотографию для блога',
                'verbose_name_plural': 'Добавить фотографию для номера',
            },
        ),
    ]
