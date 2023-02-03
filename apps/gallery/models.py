from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = models.ImageField(max_length=255,verbose_name="Фотография")
    
    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галерея"