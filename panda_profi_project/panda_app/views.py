from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.views.generic.base import View

from .models import PaintingChamber


class PaintingChambersView(View):
    """ Список покрасочных камер """
    def get(self, request):
        painting_chambers = PaintingChamber.objects.all()
        return render(request, "panda_app/painting_chambers.html", {"pc_list": painting_chambers})


class PaintingChamberDetailView(View):
    """ Полное описание покрасочной камеры """
    def get(self, request, pk):
        painting_chamber = PaintingChamber.objects.get(id=pk)
        return render(request, "panda_app/painting_chamber_detail.html", {"pc": painting_chamber})


# categories = {1: "masts",
#               2: "vimes",
#               3: "painting_chambers",
#               4: "pneumatic_presses"}
categories = {"masts": "Мачты",
                   "vimes": "Ваймы",
                   "painting_chambers": "Покрасочные камеры",
                   "pneumatic_presses": "Пневматические прессы"}
# Create your views here.


def templ_test(request):
    return HttpResponse(render_to_string("panda_app/info_page.html"))


def panda(request):
    # mast_url = reverse("product_groups", args=["masts"])
    result_str = ""
    for category in categories:
        url = reverse("product_groups", args=[category])
        result_str += f"<div class='navbar'> <div> <a href='{url}'> {categories[category]} </a> </div> "
    return HttpResponse(result_str)

# def masts(request):
#     return HttpResponse("mast")
#
# def vimes(request):
#     return HttpResponse("vime")
#
# def painting_chambers(request):
#     return HttpResponse("painting_chamber")
#
# def pytjies(request):
#     return HttpResponse("pneumatic_press")

def get_product_group(request, product_group: str):
    if product_group not in categories:
        return HttpResponseNotFound("Product not found")
    return render(request, "panda_app/info_page.html", context={"name": product_group})

# def page_for_redirection(request):
#     return HttpResponseRedirect("/panda/")
