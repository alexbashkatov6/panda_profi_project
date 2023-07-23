from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.panda),
    path('pc', views.PaintingChambersView.as_view()),
    path('<int:pk>', views.PaintingChamberDetailView.as_view()),
    # path('templ_test', views.templ_test),
    # path('<str:product_group>/', views.get_product_group, name="product_groups"),
]
