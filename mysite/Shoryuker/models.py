from django.db import models

# Create your models here.
class users(models.Model):
    user_name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.user_nameS
