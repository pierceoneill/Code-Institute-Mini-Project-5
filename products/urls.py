from django.urls import path, include
from accounts import urls as urls_accounts
from .views import all_products

urlpatterns = [
    path('', all_products, name='products'),
]
