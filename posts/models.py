"""Posts models."""

#Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#para importar el modelo profile, en el siguiente ejemplo lo hicimos de la sguiente forma
class Post(models.Model):
    """Post model class for post"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='posts/photo')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by @{self.user}'


