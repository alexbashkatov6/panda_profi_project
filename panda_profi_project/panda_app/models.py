from django.db import models
from django.urls import reverse
# from views import

# ------------------------------------------  Категории  ------------------------------------------


class Category(models.Model):
    """ Категории """
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def get_all_menu_subcategories(self):
        return MenuCategory.objects.filter(category=self)

# ------------------------------------------  Подкатегории меню ------------------------------------------


class MenuCategory(models.Model):
    """ Подкатегории """
    name = models.CharField("Подкатегория", max_length=150)  # related_name="category",
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name


class PaintingChamberMenuCategory(MenuCategory):
    """ Подкатегории окрасочных камер """
    # name = models.CharField("Подкатегория окрасочных камер", max_length=150)

    class Meta:
        verbose_name = "Подкатегория окрасочных камер"
        verbose_name_plural = "Подкатегории окрасочных камер"

    def __str__(self):
        return self.name


class VimeMenuCategory(MenuCategory):
    """ Подкатегории вайм """
    # name = models.CharField("Подкатегория вайм", max_length=150)

    class Meta:
        verbose_name = "Подкатегория вайм"
        verbose_name_plural = "Подкатегории вайм"

    def __str__(self):
        return self.name


class RollerTableMenuCategory(MenuCategory):
    """ Подкатегории рольгангов """
    # name = models.CharField("Подкатегория рольгангов", max_length=150)

    class Meta:
        verbose_name = "Подкатегория рольгангов"
        verbose_name_plural = "Подкатегории рольгангов"

    def __str__(self):
        return self.name


class GrindingTableMenuCategory(MenuCategory):
    """ Подкатегории шлифовальных столов """
    # name = models.CharField("Подкатегория шлифовальных столов", max_length=150)

    class Meta:
        verbose_name = "Подкатегория шлифовальных столов"
        verbose_name_plural = "Подкатегории шлифовальных столов"

    def __str__(self):
        return self.name


class AssemblyTableMenuCategory(MenuCategory):
    """ Подкатегории столов для сборки """
    # name = models.CharField("Подкатегория столов для сборки", max_length=150)

    class Meta:
        verbose_name = "Подкатегория столов для сборки"
        verbose_name_plural = "Подкатегории столов для сборки"

    def __str__(self):
        return self.name


class FinishedProductsMenuCategory(MenuCategory):
    """ Подкатегории готовой продукции из металла """
    # name = models.CharField("Подкатегория готовой продукции из металла", max_length=150)

    class Meta:
        verbose_name = "Подкатегория готовой продукции из металла"
        verbose_name_plural = "Подкатегории готовой продукции из металла"

    def __str__(self):
        return self.name


class ServiceMenuCategory(MenuCategory):
    """ Подкатегории услуг """
    # name = models.CharField("Подкатегория услуг", max_length=150)

    class Meta:
        verbose_name = "Подкатегория услуг"
        verbose_name_plural = "Подкатегории услуг"

    def __str__(self):
        return self.name

# ------------------------------------------  Продукты  ------------------------------------------


class Product(models.Model):
    """ Продукты """
    # main_menu_category = models.ForeignKey(MenuCategory, verbose_name="Подкатегория",
    #                                        on_delete=models.SET_NULL, null=True)
    title = models.CharField("Название", max_length=150)
    # category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    price = models.PositiveSmallIntegerField("Цена, руб", blank=True, null=True)

    main_photo = models.ImageField("Изображение", upload_to="painting_chambers/")
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)
    description = models.TextField("Описание", blank=True, null=True)

    is_front_of_category = models.BooleanField("Титульный представитель категории", default=False)

    def __str__(self):
        return self.title


class PaintingChamber(Product):
    """ Покрасочные камеры """
    main_menu_category = models.ForeignKey(PaintingChamberMenuCategory, verbose_name="Подкатегория окрасочных камер",
                                           on_delete=models.SET_NULL, null=True)

    workzone_width = models.PositiveSmallIntegerField("Ширина рабочей зоны, мм", blank=True, null=True)
    overage_body_width = models.PositiveSmallIntegerField("Общая ширина корпуса, мм", blank=True, null=True)
    overage_body_height = models.PositiveSmallIntegerField("Высота корпуса, мм", blank=True, null=True)
    overage_body_depth = models.PositiveSmallIntegerField("Глубина корпуса, мм", blank=True, null=True)
    workzone = models.PositiveSmallIntegerField("Рабочая зона, мм", blank=True, null=True)
    light_power = models.CharField("Мощность ламп освещения, Вт", blank=True, null=True, max_length=150)
    fan_performance = models.PositiveSmallIntegerField("Производительность вентилятора, куб.м/час", blank=True, null=True)
    fan_power = models.CharField("Мощность вентиляторов, кВт", blank=True, null=True, max_length=150)
    filter_count = models.PositiveSmallIntegerField("Количество фильтров, шт", blank=True, null=True)

    external_overages = models.CharField("Внешние габариты Д*Ш*В, мм", blank=True, null=True, max_length=150)
    bumper_height = models.CharField("Рабочая высота/ширина водяного отбойника, мм", blank=True, null=True, max_length=150)
    exhaust_vent_diameter = models.PositiveSmallIntegerField("Диаметр вытяжного отверстия на крыше камеры, мм", blank=True, null=True)
    drainage_pump_count = models.PositiveSmallIntegerField("Количество дренажных насосов, шт", blank=True, null=True)
    pump_power = models.CharField("Мощность насосов, кВт", blank=True, null=True, max_length=150)
    power_supply = models.CharField("Общая требуемая мощность, кВт", blank=True, null=True, max_length=150)
    voltage = models.PositiveSmallIntegerField("Напряжение, В", blank=True, null=True)

    class Meta:
        verbose_name = "Покрасочная камера"
        verbose_name_plural = "Покрасочные камеры"

    def get_absolute_url(self):
        return reverse("painting_chambers", kwargs={"product_subcategory": self.main_menu_category.url, "slug": self.url})


class Vimes(Product):
    """ Ваймы """
    main_menu_category = models.ForeignKey(VimeMenuCategory, verbose_name="Подкатегория вайм",
                                           on_delete=models.SET_NULL, null=True)

    blank_max_width = models.PositiveSmallIntegerField("Максимальная ширина заготовки, мм", blank=True, null=True)
    blank_max_height = models.PositiveSmallIntegerField("Максимальная высота заготовки, мм", blank=True, null=True)
    blank_max_depth = models.PositiveSmallIntegerField("Максимальная толщина заготовки, мм", blank=True, null=True)
    overall_size = models.CharField("Габаритные размеры, мм х мм х мм", max_length=150, blank=True, null=True)
    press_cylinders_stroke = models.PositiveSmallIntegerField("Ход прессовых цилиндров, мм", blank=True, null=True)
    pressure_shoe_step = models.PositiveSmallIntegerField("Шаг перестановки прижимных башмаков, мм", blank=True, null=True)
    pneumo_stand_count = models.PositiveSmallIntegerField("Кол-во вертикальных пневмостоек-упоров, шт", blank=True, null=True)
    side_cylinder_count = models.PositiveSmallIntegerField("Кол-во боковых цилиндров, шт", blank=True, null=True)
    horizontal_catch_count = models.PositiveSmallIntegerField("Кол-во механических упоров в горизонтальной плоскости, шт", blank=True, null=True)
    supply_pressure = models.CharField("Питающее давление в пневмосистеме, атм", max_length=150, blank=True, null=True)
    catch_count = models.PositiveSmallIntegerField("Кол-во упоров, шт", blank=True, null=True)
    full_max_pressure = models.PositiveSmallIntegerField("Максимальное давление, развиваемое при работе всех цилиндров, кг", blank=True, null=True)

    class Meta:
        verbose_name = "Вайма"
        verbose_name_plural = "Ваймы"


class GrindingTables(Product):
    """ Шлифовальные столы """
    main_menu_category = models.ForeignKey(GrindingTableMenuCategory, verbose_name="Подкатегория шлифовальных столов",
                                           on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Шлифовальный стол"
        verbose_name_plural = "Шлифовальные столы"


class RollerTables(Product):
    """ Рольганги """
    main_menu_category = models.ForeignKey(RollerTableMenuCategory, verbose_name="Подкатегория рольгангов",
                                           on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Рольганг"
        verbose_name_plural = "Рольганги"


class AssemblyTables(Product):
    """ Столы для сборки """
    main_menu_category = models.ForeignKey(AssemblyTableMenuCategory, verbose_name="Подкатегория сборочных столов",
                                           on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Стол для сборки"
        verbose_name_plural = "Столы для сборки"


class FinishedProducts(Product):
    """ Готовая продукция из металла """
    main_menu_category = models.ForeignKey(FinishedProductsMenuCategory, verbose_name="Подкатегория готовой продукции",
                                           on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Готовая продукция из металла"
        verbose_name_plural = "Готовая продукция из металла"


class FireStairs(FinishedProducts):
    """ Пожарные лестницы """
    class Meta:
        verbose_name = "Пожарная лестница"
        verbose_name_plural = "Пожарные лестницы"


class Masts(FinishedProducts):
    """ Мачты """
    class Meta:
        verbose_name = "Мачта"
        verbose_name_plural = "Мачты"


class Hatches(FinishedProducts):
    """ Люки """
    class Meta:
        verbose_name = "Люк"
        verbose_name_plural = "Люки"


class Shelvings(FinishedProducts):
    """ Стеллажи """
    class Meta:
        verbose_name = "Стеллаж"
        verbose_name_plural = "Стеллажи"


class Pyramids(FinishedProducts):
    """ Пирамиды для материалов """
    class Meta:
        verbose_name = "Пирамида для материалов"
        verbose_name_plural = "Пирамиды для материалов"


class Ramps(FinishedProducts):
    """ Пандусы """
    class Meta:
        verbose_name = "Пандус"
        verbose_name_plural = "Пандусы"


class Furnitures(FinishedProducts):
    """ Мебель """
    class Meta:
        verbose_name = "Мебель"
        verbose_name_plural = "Мебель"


class Gates(FinishedProducts):
    """ Ворота """
    class Meta:
        verbose_name = "Ворота"
        verbose_name_plural = "Ворота"


class Doors(FinishedProducts):
    """ Двери """
    class Meta:
        verbose_name = "Дверь"
        verbose_name_plural = "Двери"


class Fences(FinishedProducts):
    """ Ограждения и барьеры """
    class Meta:
        verbose_name = "Ограждения и барьеры"
        verbose_name_plural = "Ограждения и барьеры"


class Services(Product):
    """ Услуги """
    main_menu_category = models.ForeignKey(ServiceMenuCategory, verbose_name="Подкатегория услуг",
                                           on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class PaintingOfCarRims(Services):
    """ Покраска автомобильных дисков """
    class Meta:
        verbose_name = "Покраска автомобильных дисков"
        verbose_name_plural = "Покраска автомобильных дисков"


class GateInstallation(Services):
    """ Установка ворот """
    class Meta:
        verbose_name = "Установка ворот"
        verbose_name_plural = "Установка ворот"

# ------------------------------------------  Изображения товаров  ------------------------------------------


class ProductPhoto(models.Model):
    """ Изображение товара """
    name = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    main_photo = models.ImageField("Изображение", upload_to="product_images/")
    product = models.ForeignKey(Product, verbose_name="Товар", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение товара"
        verbose_name_plural = "Изображения товаров"
