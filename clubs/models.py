from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse


class Club(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
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
    
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Player(models.Model):
    slug = slug = models.SlugField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    jersey_number = models.IntegerField(default=1)
    date_of_date = models.DateField()
    nationality = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    player_image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name + ' - ' + self.nationality

    def get_absolute_url(self):
        return reverse('player-detail', kwargs={
            'slug': self.slug
        })