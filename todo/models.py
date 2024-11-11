from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(null=True, max_length=200)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title