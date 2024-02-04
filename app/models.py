from django.db import models

# Create your models here.
class Paste(models.Model):
    text = models.TextField()
    key = models.CharField(max_length=20)
    title = models.CharField(max_length=30, default='Pastebin')
    author = models.CharField(max_length=20, default="Anonymous")
    description = models.CharField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title + "(" + self.key + ")"
