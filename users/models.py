"""USER Models  """
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    """Profile models.
    Proxy models that extends the base data with other information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(null=True, blank=True)
    biography = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    picture = models.ImageField(upload_to='users/pictures', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    # def get_absolute_url(self):
    #     return reverse('users:detail', kwargs={'username': self.user.username})


    def __str__(self):
        return self.user.username

