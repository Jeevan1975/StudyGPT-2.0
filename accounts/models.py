from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.email