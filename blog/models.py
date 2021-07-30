from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


class BlogPost(models.Model):
    title = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(null=False, unique=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
