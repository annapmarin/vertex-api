from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=200)
    discipline = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('poetry', 'poesia'),
        ('painting', 'pintura'),
        ('sculpture', 'escultura'),
        ('music', 'música'),
        ('dance', 'dança'),
        ('theater', 'teatre'),
        ('ceramics', 'ceràmica'),
        ('photography', 'fotografia'),
        ('literature', 'literatura'),
        ('cinema', 'cinema'),
        ('cooking', 'cuina'),
        ('comics', 'còmic'),
        ('fashion', 'moda'),
        ('crafts', 'manualitats'),
        ('design', 'disseny'),
        ('technology', 'tecnologia'),
        ('writing', 'escriptura'),
        ('sports', 'esports'),
        ('gaming', 'jocs'),
        ('other', 'altres'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='esdeveniments')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='esdeveniments')

    def __str__(self):
        return self.title