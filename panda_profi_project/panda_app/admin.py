from django.contrib import admin

# Register your models here.
from .models import Category, PaintingChamber, Vimes, ProductPhoto, PaintingChamberMenuCategory, VimeMenuCategory, \
    RollerTableMenuCategory, GrindingTableMenuCategory, AssemblyTableMenuCategory, FinishedProductsMenuCategory, \
    ServiceMenuCategory, RollerTables, GrindingTables, AssemblyTables, FireStairs, Masts, Hatches, Shelvings, \
    Pyramids, Ramps, Furnitures, Gates, Doors, Fences, PaintingOfCarRims, GateInstallation

# admin.site.register(Category)
#
# admin.site.register(PaintingChamberMenuCategory)
# admin.site.register(VimeMenuCategory)
# admin.site.register(RollerTableMenuCategory)
# admin.site.register(GrindingTableMenuCategory)
# admin.site.register(AssemblyTableMenuCategory)
# admin.site.register(FinishedProductsMenuCategory)
# admin.site.register(ServiceMenuCategory)

admin.site.register(PaintingChamber)
admin.site.register(Vimes)
admin.site.register(RollerTables)
admin.site.register(GrindingTables)
admin.site.register(AssemblyTables)

admin.site.register(FireStairs)
admin.site.register(Masts)
admin.site.register(Hatches)
admin.site.register(Shelvings)
admin.site.register(Pyramids)
admin.site.register(Ramps)
admin.site.register(Furnitures)
admin.site.register(Gates)
admin.site.register(Doors)
admin.site.register(Fences)

admin.site.register(PaintingOfCarRims)
admin.site.register(GateInstallation)

# admin.site.register(ProductPhoto)
