from django.db import models
from django.conf import settings

class TodoList(models.Model):
    task = models.CharField(max_length=100)
    CHOISE = (
        ('Doing','нужно сделать'),
        ('Done','сделано'),
        ('canceled','отменено')
        )
    status = models.CharField(
        max_length=20, 
        choices=CHOISE,
        default='doing',
        )

    def __str__(self):
        return self.task
