from django.urls import path

from .views import card, add_cart, remove, service_teach

urlpatterns = [
    path('udemy-cart', card, name='cart'),
    path('udemy-add-cart/<int:pk>', add_cart, name='add'),
    path('udemy-remove-cart/<slug:slug>', remove, name='remove'),
    path('udemy-service-teach', service_teach, name='teach')
    
]
