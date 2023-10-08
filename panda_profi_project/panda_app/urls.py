from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.panda),
    path('main', views.MainView.as_view(), name="main"),
    path('<str:product_category>/<str:product_subcategory>', views.CategoryView.as_view(), name="all_prod_in_category"),
    path('about', views.AboutView.as_view(), name="about"),
]

for cat_name in views.dict_category_to_detail_view_cls:
    urlpatterns.append(path(f'{cat_name}/<str:product_subcategory>/<slug:slug>', views.dict_category_to_detail_view_cls[cat_name].as_view(), name=cat_name))


    # path('dry_painting_chambers', views.DryPaintingChamberView.as_view(), name="dry_painting_chambers"),
    # path('wet_painting_chambers', views.WetPaintingChamberView.as_view(), name="wet_painting_chambers"),
    # path('<slug:slug>', views.PaintingChamberDetailView.as_view(), name="pc_detail"),
    # path('templ_test', views.templ_test),
    # path('<str:product_group>/', views.get_product_group, name="product_groups"),
# urlpatterns.append(path('<str:product_category>/<str:product_subcategory>/all', views.CategoryView.as_view(), name="url_name"))