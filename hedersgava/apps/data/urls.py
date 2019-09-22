from django.urls import path
from apps.data.views import DataRetrieveAPIView, DataListCreateAPIView

app_name = 'data'

urlpatterns = [
    path('data', DataListCreateAPIView.as_view(), name='list_create_api'),
    path('data/<int:pk>', DataRetrieveAPIView.as_view(), name='detail_api'),
]
