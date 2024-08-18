from django.urls import path
from .views import detail_view

app_name = 'show_details'

urlpatterns = [
    path('<str:festival_name>/', detail_view, name='detail_view'),  # 상세 페이지 경로
]
