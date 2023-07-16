from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.panda),
    path('templ_test', views.templ_test),
    path('<str:product_group>/', views.get_product_group, name="product_groups"),
]
