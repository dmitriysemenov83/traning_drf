from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(max_length=250, verbose_name='описание')


class Meta:
    verbose_name = 'Машина'
    verbose_name_plural = 'Машины'
