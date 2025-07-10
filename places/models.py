from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Название", max_length=200)
    short_description = models.TextField("Краткое описание", blank=True)
    long_description = HTMLField("Описание", blank=True)
    latitude = models.FloatField("Широта")
    longitude = models.FloatField("Долгота")

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField("Картинки")
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        verbose_name="Место",
        related_name="images"
    )
    ordinal_number = models.PositiveIntegerField(
        "Порядковый номер",
        default=0,
        db_index=True,
    )

    class Meta:
        verbose_name = "Картинка"
        verbose_name_plural = "Картинки"
        ordering = ["ordinal_number"]

    def __str__(self):
        return f"{self.ordinal_number} {self.place.title}"
