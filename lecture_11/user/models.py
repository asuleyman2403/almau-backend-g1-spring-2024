from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    avatar = models.ImageField(upload_to='user/', null=True, max_length=2000)
    bio = models.TextField(max_length=2000, null=False, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    resume = models.FileField(upload_to='user/', null=True, max_length=2000)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.id} {self.owner.username}'




