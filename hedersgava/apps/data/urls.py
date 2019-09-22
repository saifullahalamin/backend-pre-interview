from django.urls import path
from .views import DataRetrieveAPIView

app_name = 'data'

urlpatterns = [
    path('data/<int:pk>', DataRetrieveAPIView.as_view(), name='detail_api'),
]
