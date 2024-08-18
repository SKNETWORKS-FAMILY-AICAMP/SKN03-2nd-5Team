# show_hotplace/urls.py

from django.urls import path
from .views import main_view, click_address

urlpatterns = [
    path('', main_view, name='main_view'),
    path('<str:title>',click_address, name="detail_result"),
    #path('festival/<str:festival_name>/', festival_details, name='festival_details'),
]
