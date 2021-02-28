from django.db import models


class Task(models.Model):
    name = models.CharField('Название задачи', max_length=50)
    task = models.TextField('Описание задачи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


