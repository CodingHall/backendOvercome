from django.db import models

# Create your models here.

class User(models.Model):
    name = models.TextField()
    email = models.EmailField()
    password = models.TextField()

class Writer(models.Model):
    name = models.TextField()
    email = models.EmailField()

class Article(models.Model):
    name = models.TextField()
    writer = models.OneToOneField(Writer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    last_edited = models.DateField(auto_now=True)
    title = models.TextField()
    subtitle = models.TextField()
    image = models.FileField(null=True, blank=True)
    body = models.TextField()

class Favorites_users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Bookmark_users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


