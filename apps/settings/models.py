from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank = True, null = True
    )
    logo = models.ImageField(
        upload_to="logos/",
        verbose_name="Логотип сайта"
    )
    
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка сайта"
        verbose_name_plural = "Настройки сайта"
        
        
class Slide(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название слайда")
    descriptions = models.TextField(verbose_name="Описание для слайда")
    image = models.ImageField(upload_to="slide/", verbose_name="Фотография для слайда")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка слайда"
        verbose_name_plural = "Настройки слайда"
        
class Partners(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назваие партнера")
    logo = models.ImageField(upload_to="partners/", verbose_name="Логотип партнера")
    url = models.URLField(verbose_name="Ссылка на них")
    
    class Meta:
        verbose_name = "Наш партнер"
        verbose_name_plural = "Наши  партнеры"