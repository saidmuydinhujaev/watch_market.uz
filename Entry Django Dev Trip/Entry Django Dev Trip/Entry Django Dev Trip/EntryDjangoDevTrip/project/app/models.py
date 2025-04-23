from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя автора")
    picture = models.ImageField(upload_to='authors/', verbose_name="Фото автора")
    bio = models.TextField(blank=True, verbose_name="Биография")

    def __str__(self):
        return self.name


class Watch(models.Model):
    BRAND_CHOICES = [
        ('Rolex', 'Rolex'),
        ('Casio', 'Casio'),
        ('Apple', 'Apple'),
        ('Samsung', 'Samsung'),
    ]

    GENDER_CHOICES = [
        ('men', 'Мужские'),
        ('women', 'Женские'),
        ('unisex', 'Унисекс'),
    ]

    MATERIAL_CHOICES = [
        ('plastic', 'Пластик'),
        ('aluminum', 'Алюминий'),
        ('steel', 'Нержавеющая сталь'),
    ]

    WATERPROOF_CHOICES = [
        ('yes', 'Да'),
        ('no', 'Нет'),
    ]

    MECHANISM_CHOICES = [
        ('mechanical', 'Механические'),
        ('automatic', 'Автоматические'),
        ('quartz', 'Кварцевые'),
    ]

    title = models.CharField(max_length=100, verbose_name="Название")
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, verbose_name="Бренд")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Пол")
    material = models.CharField(max_length=100, choices=MATERIAL_CHOICES, verbose_name="Материал")
    water_resistance = models.CharField(max_length=50, choices=WATERPROOF_CHOICES, verbose_name="Водостойкость")
    movement = models.CharField(max_length=50, choices=MECHANISM_CHOICES, verbose_name="Механизм")
    image = models.ImageField(upload_to='watches/', blank=True, null=True, verbose_name="Изображение")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='watches', verbose_name="Автор", null=True)
    video = models.FileField(
        upload_to='watch_videos/',
        blank=True,
        null=True,
        verbose_name="Видео часов",
        help_text="Загрузите MP4/MOV видео (макс. 100MB)"
    )

    def __str__(self):
        return f"{self.get_brand_display()} {self.title}"

    def get_absolute_url(self):
        return reverse('watch_detail', kwargs={'pk': self.pk})
    

class WatchImage(models.Model):
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='watches/gallery/')
    is_main = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']

    class Meta:
        verbose_name = "Изображение часов"
        verbose_name_plural = "Изображения часов"

    def __str__(self):
        return f"Изображение для {self.watch}"