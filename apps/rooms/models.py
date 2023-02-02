from django.db import models

# Create your models here.
class Room(models.Model):
    title = models.CharField(max_length=255,verbose_name="О номере")
    descriptions = models.TextField(verbose_name="Описание о номере")
    price = models.CharField(max_length=255,verbose_name="Цена номера")
    
    service = models.CharField(max_length=255,verbose_name="Оценка услуг от 1 до 5")
    comfort = models.CharField(max_length=255,verbose_name="Оценка комфорта от 1 до 5")
    location = models.CharField(max_length=255,verbose_name="Оценка чистоты от 1 до 5")
    
    amenities1 = models.CharField(max_length=255,verbose_name="Первое удобство", blank=True, null=True)
    amenities2 = models.CharField(max_length=255,verbose_name="Второе удобство", blank=True, null=True)
    amenities3 = models.CharField(max_length=255,verbose_name="Третье удобство", blank=True, null=True)
    amenities4 = models.CharField(max_length=255,verbose_name="Четвертое удобство", blank=True, null=True)
    amenities5 = models.CharField(max_length=255,verbose_name="Пятое удобство", blank=True, null=True)
    amenities6 = models.CharField(max_length=255,verbose_name="Шестое удобство", blank=True, null=True)
    
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
        
class BackroundRoom(models.Model):
    image = models.ImageField(upload_to="backround/", verbose_name="Задний фон")
    
    class Meta:
        verbose_name = "Задний фон страницы <<Наши номера>>"
        verbose_name_plural = "Задний фон страницы  <<Наши номера>>"
    
class Comment(models.Model):
    name = models.CharField(max_length=255,verbose_name="Имя")
    email = models.EmailField(verbose_name="Почта")
    message = models.TextField(verbose_name="Коментарий")
    post = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="post_comment")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created",)
        verbose_name = "Комментрии к номерам"
        verbose_name_plural = "Комментрии к номерам"
        