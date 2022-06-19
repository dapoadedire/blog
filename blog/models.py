from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True)

    def summary(self):
        return self.content[:100]
    def str(self):
        return f"self.title | self.author.username"

    