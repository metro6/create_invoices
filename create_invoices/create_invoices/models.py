# from django.db import models
#
#
# class Invoice(models.Model):
#     name = models.CharField(verbose_name="Название формы", max_length=128)
#     text = models.TextField(verbose_name="Предзаполненный список", max_length=5000)
#     image = models.ImageField(verbose_name="Фото продукта", upload_to='covers')
#
#     class Meta:
#         verbose_name = "Форма продукта"
#         verbose_name_plural = "Формы продуктов"
#
#
#     def __str__(self):
#         return self.name