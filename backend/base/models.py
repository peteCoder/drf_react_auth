from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=False)
    body = models.TextField()
    
    def __str__(self):
        return self.body
    
    
    
    


