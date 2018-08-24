from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfileInfo(models.Model):
    #this is one to one relationship
    user = models.OneToOneField(User, on_delete=True)

    # additional info
    portfolio_site = models.URLField(blank=True)
    image = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username