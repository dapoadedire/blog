from ckeditor.fields import RichTextField
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    title = models.CharField(max_length=200)
    content = RichTextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_published = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images/', blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="draft"
    )
    slug = models.SlugField(max_length=50, unique=True, editable=False)

    def summary(self):
        return self.content[:100]

    def __str__(self):
        return self.title | self.author.username

    class Meta:
        ordering = ("-date_published",)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        pass 
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

