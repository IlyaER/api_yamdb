from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet

app_name = 'api'

router = routers.DefaultRouter()
# router.register(
#     r'posts/(?P<post_id>\d+)/comments',
#     CommentViewSet,
#     basename='comments',
# )
# router.register('posts', PostViewSet)
# router.register('groups', GroupViewSet)
# router.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/', include('djoser.urls.jwt')),
]
