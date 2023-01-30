from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255,verbose_name="О нас")
    descriptions = models.TextField(verbose_name="Описание о нас")
    image1 = models.ImageField(upload_to="about", verbose_name="Первая фотография о нас", blank=True, null=True)
    image2 = models.ImageField(upload_to="about", verbose_name="Вторая фотография о нас", blank=True, null=True)
    image3 = models.ImageField(upload_to="about", verbose_name="Третья фотография о нас", blank=True, null=True)
    image4 = models.ImageField(upload_to="about", verbose_name="Четвертая фотография о нас", blank=True, null=True)
    image5 = models.ImageField(upload_to="about", verbose_name="Пятая фотография о нас", blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Настройка О нас"
        verbose_name_plural = "Настройки О нас"
        
class BackroundAbout(models.Model):
    image = models.ImageField(upload_to="backround/", verbose_name="Задний фон")
    
    class Meta:
        verbose_name = "Задний фон страницы <<О нас>>"
        verbose_name_plural = "Задний фон страницы <<О нас>>"
        