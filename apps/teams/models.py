from django.db import models

# Create your models here.
class Team(models.Model):
    image = models.ImageField(upload_to="team", verbose_name="Фотография сотрудника")
    name = models.CharField(max_length=255,verbose_name="Имя сотрудника", blank = True, null = True)
    work = models.CharField(max_length=255,verbose_name="Должность сотрудника", blank = True, null = True)
    instagram = models.URLField(verbose_name="Instagram сотрудника", blank = True, null = True)
    whatsapp = models.URLField(verbose_name=" Whatsapp сотрудника", blank = True, null = True)
    Facebook = models.URLField(verbose_name="Facebook  сотрудника", blank = True, null = True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Наша команда"
        verbose_name_plural = "Наша команда"
        
class BackroundTeam(models.Model):
    image = models.ImageField(upload_to="backround/", verbose_name="Задний фон")
    
    class Meta:
        verbose_name = "Задний фон страницы <<Наша команда>>"
        verbose_name_plural = "Задний фон страницы <<Наша комана>>"