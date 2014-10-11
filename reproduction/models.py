from django.db import models

# Create your models here.


class TestModel(models.Model):
    foo = models.CharField(max_length=32)