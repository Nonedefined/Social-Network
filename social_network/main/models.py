from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Account(AbstractUser):
    username = models.SlugField(unique=True)
    bio = models.CharField(max_length=300, blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    mobile = models.PositiveBigIntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='account_photo/%Y/%m/%d/', blank=True, default="account_photo/default.jpg")

    def get_absolute_url(self):
        return reverse("view_user", kwargs={"user_id": self.pk})


class Post(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to='post_photo/%Y/%m/%d/', blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("view_post", kwargs={"post_id": self.pk})

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.text}"


class PostComment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PostLike(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    is_liked = models.BooleanField(default=False)


class Chat(models.Model):
    user = models.ManyToManyField(Account, null=True)


class MessageChat(models.Model):
    text = models.TextField()
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
