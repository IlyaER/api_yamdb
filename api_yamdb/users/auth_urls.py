from django.urls import path

from users.views import get_token, send_code

urlpatterns = [
    path('signup/', send_code, name='send_code'),
    path('token/', get_token, name='get_token')
]
