from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse


class Club(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=50)
    ground = models.CharField(max_length=70)
    founded_date = models.DateField()
    official_website = models.URLField(max_length=70)
    logo = models.ImageField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('club-detail', kwargs={
            'slug': self.slug
        })