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
        