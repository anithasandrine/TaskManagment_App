from django.db import models

class Tasks(models.Model):
    statusChoice =(
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('In Progress', 'In Progress')
    )
    
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=250, choices=statusChoice,default='Pending')
    updadeted = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
        
    
