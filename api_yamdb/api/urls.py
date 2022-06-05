from django.urls import include, path
from rest_framework import routers

from .views import (
    UserViewSet, CommentViewSet, ReviewViewSet, TitleViewSet, GenreViewSet,
    CategoryViewSet, get_token, send_code,
)

app_name = 'api'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('titles', TitleViewSet)
router.register('genres', GenreViewSet)
router.register('categories', CategoryViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews',
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', send_code, name='send_code'),
    path('v1/auth/token/', get_token, name='get_token')
]
