from rest_framework import routers

from .viewsets import *

router = routers.SimpleRouter()
router.register('users', UserViewSet)
router.register('writers', WriterViewSet)
router.register('articles', ArticleViewSet)
router.register('favorites', FavoriteViewSet)
router.register('bookmarks', BookmarkViewSet)

urlpatterns = router.urls