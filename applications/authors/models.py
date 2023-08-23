from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(verbose_name='name', max_length=200)

    def __str__(self):
        return f"Author: {self.name}"
