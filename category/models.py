from django.db import models

class Category(models.Model):
    CategoryName = models.CharField(max_length=50)
    
  
    def __str__(self):
        return self. CategoryName

