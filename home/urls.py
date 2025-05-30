from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('products/', views.products, name='products'),
    path('products/<slug:brand_slug>/<slug:product_slug>/', views.product_detail, name='product_detail')
]