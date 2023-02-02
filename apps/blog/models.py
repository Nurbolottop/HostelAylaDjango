from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255,verbose_name="О Блоге")
    descriptions = models.TextField(verbose_name="Описание о Блоге")
    blog_time = models.DateTimeField(auto_now_add = True)

    
    image1 = models.ImageField(upload_to="about", verbose_name="Первая фотография блога", blank=True, null=True)
    image2 = models.ImageField(upload_to="about", verbose_name="Вторая фотография блога", blank=True, null=True)
    image3 = models.ImageField(upload_to="about", verbose_name="Третья фотография блога", blank=True, null=True)
    image4 = models.ImageField(upload_to="about", verbose_name="Четвертая фотография блога", blank=True, null=True)
    image5 = models.ImageField(upload_to="about", verbose_name="Пятая фотография блога", blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.descriptions}"
    
    class Meta:
        verbose_name = "Настройка Блога"
        verbose_name_plural = "Настройки Новостей"
        
class BackroundBlog(models.Model):
    image = models.ImageField(upload_to="backround/", verbose_name="Задний фон")
    
    class Meta:
        verbose_name = "Задний фон страницы <<Наш Блог>>"
        verbose_name_plural = "Задний фон страницы  <<Наш Блог>>"
        
class Comment(models.Model):
    name = models.CharField(max_length=255,verbose_name="Имя")
    email = models.EmailField(verbose_name="Почта")
    message = models.TextField(verbose_name="Коментарий")
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="post_comment")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ("-created",)
        verbose_name = "Комментрии к новостям"
        verbose_name_plural = "Комментрии к новостям"
        