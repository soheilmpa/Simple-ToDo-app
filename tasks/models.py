from django.db import models

# Create your models here.

class Task(models.Model):
    """
        docstring for Task
    """
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

