from django.db import models

from where_to_go.settings import MEDIA_URL


class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание', blank=True)
    description_long = models.TextField('Описание', blank=True)
    latitude = models.FloatField('Широта')
    longitude = models.FloatField('Долгота')
    place_id = models.CharField('ID места', max_length=200, null=True)

    def __str__(self):
        return self.title
    
    @property
    def get_absolute_image_url(self):
        return '%s%s' % (MEDIA_URL, self.image.url)