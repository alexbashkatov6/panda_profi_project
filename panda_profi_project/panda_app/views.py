from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView, View

from .models import PaintingChamber, Category, PaintingChamberMenuCategory, Product, MenuCategory, Vimes, RollerTables, \
    AssemblyTables, FinishedProducts, Services, GrindingTables

dict_category_to_model_cls = {"painting_chambers": PaintingChamber,
                              "vimes": Vimes,
                              "services": Services,
                              "finished_products": FinishedProducts,
                              "assembly_tables": AssemblyTables,
                              "grinding_tables": GrindingTables,
                              "roller_tables": RollerTables}


class MenuCategories(object):
    """ Список категорий """

    def get_all_categories(self):
        return Category.objects.all()


class AboutView(MenuCategories, View):
    """ Список всех подкатегорий """

    def get(self, request):
        return render(request, "panda_app/about.html", {"view": self})


class MainView(MenuCategories, View):
    """ Список всех подкатегорий """

    def get(self, request):
        title_product_list = []
        for category in Category.objects.all():
            for subcategory in category.get_all_menu_subcategories():
                for key in dict_category_to_model_cls:
                    cls = dict_category_to_model_cls[key]
                    candidates = cls.objects.filter(main_menu_category=subcategory)
                    check_exist = candidates.filter(is_front_of_category=True)
                    if len(check_exist) > 1:
                        title_product = candidates[0]
                        title_product_list.append(title_product)
                    elif check_exist:
                        # print("check_exist")
                        title_product = candidates.get(is_front_of_category=True)
                        title_product_list.append(title_product)
        # painting_chambers = PaintingChamber.objects.all()
        return render(request, "panda_app/categories.html",
                      {"title_products_list": title_product_list,
                       "view": self})


class CategoryView(MenuCategories, View):
    """ Список покрасочных камер """

    def get(self, request, product_category: str, product_subcategory: str):
        prod_list = dict_category_to_model_cls[product_category].objects.filter(draft=False, main_menu_category=MenuCategory.objects.get(
                                                                                        url=product_subcategory))
        product_subcategory_rus = "Неизвестная категория"
        subcat_list = MenuCategory.objects.get(url=product_subcategory)
        if subcat_list:
            product_subcategory_rus = str(subcat_list)
        return render(request, "panda_app/all_products_in_category.html",
                      {"product_list": prod_list,
                       "product_category": product_category,
                       "product_subcategory": product_subcategory,
                       "product_subcategory_rus": product_subcategory_rus,
                       "view": self})


class PaintingChamberDetailView(MenuCategories, DetailView):
    """ Полное описание покрасочной камеры """
    model = PaintingChamber
    template_name = "panda_app/painting_chamber_detail.html"
    slug_field = "url"
    context_object_name = 'prod'


class VimesDetailView(MenuCategories, DetailView):
    """ Полное описание ваймы """
    model = Vimes
    template_name = "panda_app/vime_detail.html"
    slug_field = "url"
    context_object_name = 'prod'


class ServicesDetailView(MenuCategories, DetailView):
    """ Полное описание услуг """
    model = Services
    template_name = "panda_app/empty_detail.html"
    slug_field = "url"
    context_object_name = 'prod'


class FinishedProductsDetailView(MenuCategories, DetailView):
    """ Полное описание готовой продукции из металла """
    model = FinishedProducts
    template_name = "panda_app/empty_detail.html"
    slug_field = "url"
    context_object_name = 'prod'


class AssemblyTablesDetailView(MenuCategories, DetailView):
    """ Полное описание сборочных столов """
    model = AssemblyTables
    template_name = "panda_app/empty_detail.html"
    slug_field = "url"
    context_object_name = 'prod'


class GrindingTablesDetailView(MenuCategories, DetailView):
    """ Полное описание шлифовальных столов """
    model = GrindingTables
    template_name = "panda_app/empty_detail.html"
    slug_field = "url"
    context_object_name = 'prod'


class RollerTablesDetailView(MenuCategories, DetailView):
    """ Полное описание шлифовальных столов """
    model = RollerTables
    template_name = "panda_app/empty_detail.html"
    slug_field = "url"
    context_object_name = 'prod'


dict_category_to_detail_view_cls = {"painting_chambers": PaintingChamberDetailView,
                                    "vimes": VimesDetailView,
                                    "services": ServicesDetailView,
                                    "finished_products": FinishedProductsDetailView,
                                    "assembly_tables": AssemblyTablesDetailView,
                                    "grinding_tables": GrindingTablesDetailView,
                                    "roller_tables": RollerTablesDetailView
                                    }

categories = {"masts": "Мачты",
              "vimes": "Ваймы",
              "painting_chambers": "Покрасочные камеры",
              "pneumatic_presses": "Пневматические прессы"}


def templ_test(request):
    return HttpResponse(render_to_string("panda_app/info_page.html"))


def panda(request):
    # mast_url = reverse("product_groups", args=["masts"])
    result_str = ""
    for category in categories:
        url = reverse("product_groups", args=[category])
        result_str += f"<div class='navbar'> <div> <a href='{url}'> {categories[category]} </a> </div> "
    return HttpResponse(result_str)


def get_product_group(request, product_group: str):
    if product_group not in categories:
        return HttpResponseNotFound("Product not found")
    return render(request, "panda_app/info_page.html", context={"name": product_group})

# def page_for_redirection(request):
#     return HttpResponseRedirect("/panda/")

# from django.views.generic.base import View

# class SubcategoryProductsView(View):
#     """ Список покрасочных камер """
#     def get(self, request):
#         painting_chambers = PaintingChamber.objects.all()
#         return render(request, "panda_app/all_products_in_category.html", {"pc_list": painting_chambers})

# class PaintingChamberDetailView(View):
#     """ Полное описание покрасочной камеры """
#     # def get(self, request, pk):
#     #     painting_chamber = PaintingChamber.objects.get(id=pk)
#     def get(self, request, slug):
#         painting_chamber = PaintingChamber.objects.get(url=slug)
#         return render(request, "panda_app/painting_chamber_detail.html", {"pc": painting_chamber})

# categories = {1: "masts",
#               2: "vimes",
#               3: "painting_chambers",
#               4: "pneumatic_presses"}
