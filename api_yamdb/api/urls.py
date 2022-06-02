from django.urls import include, path
from rest_framework import routers

from api.views import get_token, send_code, UserViewSet

router = routers.DefaultRouter()
router.register(
    r'',
    UserViewSet
)
urlpatterns = [
    path('auth/signup/', send_code, name='send_code'),
    path('auth/token/', get_token, name='get_token'),
    path('users/', include(router.urls))
]
