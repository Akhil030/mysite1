from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='pics')
    language = models.CharField(max_length=20)
    module = models.CharField(max_length=20)
