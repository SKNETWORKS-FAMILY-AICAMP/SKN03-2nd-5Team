from django.urls import path
from .views import main_view, click_address

urlpatterns = [
    path('',main_view, name="main_view"),
    path('<str:title>',click_address, name="detail_result"),
]

