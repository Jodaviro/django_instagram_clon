"""USER Models  """
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    """
    Profile is an User class Proxy.
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
        return f' @{self.user.username}'



class Contact(models.Model):
    """
    Following and followers system.
    followers acces will be trough the profile model.
    eg: 'profile.followers.count' will return Contact objects
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    following= models.ManyToManyField(Profile, related_name='followers', blank=True)


    @classmethod
    def follow(cls, profile, another_profile):
        object = cls.objects.get(profile=profile)
        object.following.add(another_profile)

    @classmethod
    def unfollow(cls, profile, another_profile):
        object = cls.objects.get(profile=profile)
        object.following.remove(another_profile)

    def following_count(self):
        return self.following.count()
    
    
    def __str__(self):
        return f'profile: {self.profile}, Following : {self.following.all()}'