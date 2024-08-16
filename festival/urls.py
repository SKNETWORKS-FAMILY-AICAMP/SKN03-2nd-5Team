from django.urls import path
from .views import main,search_results, click_address

urlpatterns = [
    path('',main, name="festival-main"),
    # path('search/',search_results, name='search-results'),
    path('<str:title>',click_address, name="detail_result"),
    path('',search_results, name="search_results"),

]

