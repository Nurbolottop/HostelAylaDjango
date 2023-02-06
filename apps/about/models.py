from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255,verbose_name="О нас")
    descriptions = models.TextField(verbose_name="Описание о нас")
    
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Настройка О нас"
        verbose_name_plural = "Настройки О нас"
        
class ImageAbout(models.Model):
    about = models.ForeignKey(
        About,
        on_delete= models.CASCADE,
        related_name="about",
        verbose_name="О нас"
    )
    image = models.ImageField(upload_to="about", verbose_name="Фотография о нас", blank=True, null=True)

    def __str__(self):
        return f"{self.about} - {self.image}"
    
    class Meta:
        verbose_name = "Добавить фотографию  О нас"
        verbose_name_plural = "Добавить фотографию О нас"
        
class BackroundAbout(models.Model):
    image = models.ImageField(upload_to="backround/", verbose_name="Задний фон")
    
    class Meta:
        verbose_name = "Задний фон страницы <<О нас>>"
        verbose_name_plural = "Задний фон страницы <<О нас>>"
        
class History(models.Model):
    image = models.ImageField(
        upload_to="about_history",
        verbose_name="Фотография"
    )
    years = models.CharField(
        max_length=244,
        verbose_name="Год"
        )
    name = models.CharField(
        max_length=255,
        verbose_name="Название"
        )
    description = models.TextField(
        verbose_name="Описание"
    )
    
    def __str__(self):
        return f"{self.years}: {self.name} - {self.description}"
    
    class Meta:
        verbose_name = 'Наша история'
        verbose_name_plural = 'Наша история'
    