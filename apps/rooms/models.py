from django.db import models

# Create your models here.
class Room(models.Model):
    title = models.CharField(max_length=255,verbose_name="О номере")
    descriptions = models.TextField(verbose_name="Описание о номере")
    service = models.CharField(max_length=255,verbose_name="Оценка услуг от 1 до 5")
    comfort = models.CharField(max_length=255,verbose_name="Оценка комфорта от 1 до 5")
    location = models.CharField(max_length=255,verbose_name="Оценка локации от 1 до 5")
    service = models.CharField(max_length=255,verbose_name="Оценка услуг от 1 до 5")
    amenities1 = models.CharField(max_length=255,verbose_name="Первое удобство", blank=True, null=True)
    amenities2 = models.CharField(max_length=255,verbose_name="Второе удобство", blank=True, null=True)
    amenities3 = models.CharField(max_length=255,verbose_name="Третье удобство", blank=True, null=True)
    amenities4 = models.CharField(max_length=255,verbose_name="Четвертое удобство", blank=True, null=True)
    amenities5 = models.CharField(max_length=255,verbose_name="Пятое удобство", blank=True, null=True)
    
    image1 = models.ImageField(upload_to="about", verbose_name="Первая фотография номера", blank=True, null=True)
    image2 = models.ImageField(upload_to="about", verbose_name="Вторая фотография номера", blank=True, null=True)
    image3 = models.ImageField(upload_to="about", verbose_name="Третья фотография номера", blank=True, null=True)
    image4 = models.ImageField(upload_to="about", verbose_name="Четвертая фотография номера", blank=True, null=True)
    image5 = models.ImageField(upload_to="about", verbose_name="Пятая фотография номера", blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Настройка номера"
        verbose_name_plural = "Настройки Номеров"