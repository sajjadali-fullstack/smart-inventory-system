from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.products_view),
    path('home/', views.home_view, name='home'),
    path('add/', views.add_product_view, name='add_product'),

    # API Views
    path('api/products/', views.product_api, name='products_api'),
    path('api/clothes/', views.clothes_api, name='clothes_api'),
    path('api/electronics/', views.electronics_api, name='electronics_api'),
    path('api/furnitures/', views.furniture_api, name='furnitures_api'),
    path('api/others/', views.other_api, name='others_api'),

]
