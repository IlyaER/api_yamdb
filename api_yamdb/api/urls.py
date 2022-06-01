from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet, CommentViewSet, ReviewViewSet, TitleViewSet, get_token, send_code

app_name = 'api'

router = routers.DefaultRouter()
router.register(
    '', UserViewSet
)
router.register('users', UserViewSet)
router.register('titles', TitleViewSet)
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
    path('v1/signup/', send_code, name='send_code'),
    path('v1/token/', get_token, name='get_token')
    # path('v1/', include('djoser.urls.jwt')),
]