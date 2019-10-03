from django.db import models


class Invoice(models.Model):
    name = models.CharField(verbose_name="Название формы", max_length=128)
    text = models.TextField(verbose_name="Краткое описание", max_length=5000, null=True, blank=True)
    full_text = models.TextField(verbose_name="Полное описание", max_length=5000, null=True, blank=True)
    image = models.ImageField(verbose_name="Фото продукта", upload_to='covers', null=True, blank=True)
    departure_date = models.DateTimeField(verbose_name="Дата отправления", null=True, blank=True)
    receive_date = models.DateTimeField(verbose_name="Дата получения", null=True, blank=True)

    class Meta:
        verbose_name = "Форма продукта"
        verbose_name_plural = "Формы продуктов"

    def __str__(self):
        return self.name
