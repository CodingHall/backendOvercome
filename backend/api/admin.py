from django.contrib import admin
from .models import Writer, Article, User

# Register your models here.
admin.site.register(Writer)
admin.site.register(Article)
admin.site.register(User)