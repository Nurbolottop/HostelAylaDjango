from django.db import models

# Create your models here.
class Room(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="О номере"
        )
    descriptions = models.TextField(
        verbose_name="Описание о номере"
        )
    price = models.CharField(
        max_length=255,
        verbose_name="Цена номера"
        )
    image1 = models.ImageField(
        upload_to="room_image", 
        verbose_name="Фотография номера", 
        blank=True, null=True)
    
    service = models.CharField(
        max_length=255,
        verbose_name="Оценка услуг от 1 до 5"
        ) 
    comfort = models.CharField(
        max_length=255,
        verbose_name="Оценка комфорта от 1 до 5"
        )
    location = models.CharField(
        max_length=255,
        verbose_name="Оценка чистоты от 1 до 5"
        )
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    
    class Meta:
        verbose_name = "Наш номер"
        verbose_name_plural = "Наши Номера"
        
class Amenities(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="amenities",
        verbose_name="Выберите номер"
    )
    amenities = models.CharField(
        max_length=255,
        verbose_name="Удобство номера",
        blank=True, null=True
        )

    def __str__(self):
        return f"{self.room} - {self.amenities}"
    
    class Meta:
        verbose_name = "Добавить удобство для номера"
        verbose_name_plural = "Добавить удобство для номера"
        
class ImageRoom(models.Model):
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="image_room",
        verbose_name="Выберите номер"
    )
    image = models.ImageField(
        upload_to="about", 
        verbose_name="Фотография номера", 
        blank=True, null=True)
    
    def __str__(self):
        return f"{self.room} - {self.image}"

    class Meta:
        verbose_name = "Добавить фотографию для номера"
        verbose_name_plural = "Добавить фотографию для номера"
    

    

        
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
        