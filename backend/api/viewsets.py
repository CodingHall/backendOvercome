from rest_framework import viewsets

from .models import *
from .serializer import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = WriterSerializer

class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorites_users.objects.all()
    serializer_class = FavoriteSerializer

class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark_users.objects.all()
    serializer_class = BookmarkSerializer