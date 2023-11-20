from django.urls import path
from . import views

urlpatterns = [
    # path('', views.product_list, name='product_list'),
    path('', views.home_view, name='home'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]