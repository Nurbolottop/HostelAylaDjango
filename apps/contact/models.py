from django.db import models

# Create your models here.
class Contact(models.Model):
    phone = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер"
    )
    email = models.EmailField(
        verbose_name="Почта",
        blank = True, null = True
    )
    
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        blank = True, null = True
    )
    work = models.CharField(max_length=255,
        verbose_name="Рабочие дни",
        blank = True, null = True
    )
    work2 = models.CharField(max_length=255,
        verbose_name="Рабочое время",
        blank = True, null = True
    )
    youtube = models.URLField(
        verbose_name="Ссылка на Youtube",
        blank = True, null = True
    )
    facebook = models.URLField(
        verbose_name="Ссылка на Facebook",
        blank = True, null = True
    )
    instagram = models.URLField(
        verbose_name="Ссылка на instagram",
        blank = True, null = True
    )
    whatsapp = models.URLField(
        verbose_name="Ссылка на WhatsApp",
        blank = True, null = True
    )

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Настройка Контакта"
        verbose_name_plural = "Настройки Контактов"
        
class BackroundContact(models.Model):
    image = models.ImageField(upload_to="backround/", verbose_name="Задний фон")
    
    class Meta:
        verbose_name = "Задний фон страницы <<Контакты>>"
        verbose_name_plural = "Задний фон страницы <<Контакты>>"