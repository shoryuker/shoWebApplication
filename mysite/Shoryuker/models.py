from django.db import models
import uuid

# Create your models here.
class users(models.Model):    
    user_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.user_name

