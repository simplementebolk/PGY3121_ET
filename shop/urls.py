from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', views.buy, name='buy'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('eloboost/', views.eloboost, name='eloboost'),
    path('coaching/', views.coaching, name='coaching'),
    path('accounts/', views.accounts, name='accounts'),
    path('riot_points/', views.riot_points, name='riot_points'),
    path('cart/', views.view_cart, name='cart'),
    path('add_to_cart/<int:account_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
