from django.db import models

# Create your models here.


# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     rating = models.IntegerField()

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


class Product(models.Model):
    """ Продукты """
    title = models.CharField("Название", max_length=150)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    sub_category = models.CharField("Подкатегория", max_length=150)
    main_photo = models.ImageField("Изображение", upload_to="painting_chambers/")
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title


class PaintingChamber(Product):
    """ Покрасочные камеры """

    workzone_width = models.PositiveSmallIntegerField("Ширина рабочей зоны, мм")
    overage_body_width = models.PositiveSmallIntegerField("Общая ширина корпуса, мм")
    overage_body_height = models.PositiveSmallIntegerField("Высота корпуса, мм")
    overage_body_depth = models.PositiveSmallIntegerField("Глубина корпуса, мм")
    workzone = models.PositiveSmallIntegerField("Рабочая зона, мм")
    light_power = models.PositiveSmallIntegerField("Мощность светильников, Вт/шт")
    fan_performance = models.PositiveSmallIntegerField("Производительность вентилятора, куб.м/час")
    fan_power = models.PositiveSmallIntegerField("Мощность вентилятора, кВт")
    filter_count = models.PositiveSmallIntegerField("Количество фильтров, шт")

    application = models.TextField("Применение")
    work_principle = models.TextField("Принцип работы")
    adventages = models.TextField("Преимущества")
    cabin_equipment = models.TextField("Комплектация кабины")
    equipment_set = models.TextField("Комплектация оборудования")

    class Meta:
        verbose_name = "Покрасочная камера"
        verbose_name_plural = "Покрасочные камеры"


class Vimes(Product):
    """ Ваймы """
    blank_max_width = models.PositiveSmallIntegerField("Максимальная ширина заготовки, мм")
    blank_max_height = models.PositiveSmallIntegerField("Максимальная высота заготовки, мм")
    blank_max_depth = models.PositiveSmallIntegerField("Максимальная толщина заготовки, мм")
    overall_size = models.CharField("Габаритные размеры, мм х мм х мм", max_length=150)
    press_cylinders_stroke = models.PositiveSmallIntegerField("Ход прессовых цилиндров, мм")
    pressure_shoe_step = models.PositiveSmallIntegerField("Шаг перестановки прижимных башмаков, мм")
    pneumo_stand_count = models.PositiveSmallIntegerField("Кол-во вертикальных пневмостоек-упоров, шт")
    side_cylinder_count = models.PositiveSmallIntegerField("Кол-во боковых цилиндров, шт")
    horizontal_catch_count = models.PositiveSmallIntegerField("Кол-во механических упоров в горизонтальной плоскости, шт")
    supply_pressure = models.PositiveSmallIntegerField("Питающее давление в пневмосистеме, атм")
    catch_count = models.PositiveSmallIntegerField("Кол-во упоров, шт")
    full_max_pressure = models.PositiveSmallIntegerField("Максимальное давление, развиваемое при работе всех цилиндров, кг")

    class Meta:
        verbose_name = "Вайма"
        verbose_name_plural = "Ваймы"


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
