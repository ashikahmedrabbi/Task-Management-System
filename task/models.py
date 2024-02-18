from django.db import models
from category.models import Category



class Task(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription  = models.TextField()
    taskDate = models.DateField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    taskStatus = models.BooleanField(default=False)
    
    
    
    def __str__(self):
        return self.taskTitle


    


    
    