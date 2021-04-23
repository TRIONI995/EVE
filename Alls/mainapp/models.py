from django.db import models
from datetime import date


class Category(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Отрасль"
        verbose_name_plural = "Отрасли"


class Chin(models.Model):

    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    nick = models.CharField(max_length=25, verbose_name='Имя в игре')
    slug = models.SlugField(unique=True)
    portret = models.ImageField(verbose_name='Портрет', upload_to="chin/")
    description = models.TextField(verbose_name='Описание', null=True)
    frac = models.CharField(max_length=25, verbose_name='Корпорация ')
    discords = models.CharField(max_length=25, verbose_name='Связь Discord ')
    link = models.URLField(blank=True)

    def __str__(self):
        return self.nick

    def get_model_name(self):
        return self.__class__.__name__.lower()

    class Meta:
        verbose_name = "Чиновника"
        verbose_name_plural = "Чиновники"


class Di(models.Model):
    """Директора и заместители"""
    names = models.CharField("Имя", max_length=100)
    image = models.ImageField("Изображение", upload_to="dir/")

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = "Директора и заместителя"
        verbose_name_plural = "Директора и заместители"


class Corporation(models.Model):
    """Корпорация"""
    title = models.CharField("Название", max_length=50)
    tagline = models.CharField("Короткое название", max_length=5, default='', help_text="указывать как в eve")
    logo = models.ImageField("Логотип", upload_to="corp/")
    country = models.CharField("Страна", max_length=30)
    number = models.CharField("Численность", max_length=4)
    recruitment = models.CharField("Набор", max_length=8)
    directors = models.ManyToManyField(Di, verbose_name="Директор", related_name="corp_director")
    deputy = models.ManyToManyField(Di, verbose_name="Заместители", related_name="corp_deputy")
    world_premiere = models.DateField("Дата присоединения", default=date.today)
    act = models.CharField("Акции", max_length=30, help_text="указывать остаток")
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Корпорацию"
        verbose_name_plural = "Корпорации"


class RatingStar(models.Model):
    """Рейтинг Звезды"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Рейтинг Zkillboard"
        verbose_name_plural = "Рейтинги Zkillboard"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Рейтинг")
    corporation = models.ForeignKey(Corporation, on_delete=models.CASCADE, verbose_name="Корпорация")

    def __str__(self):
        return f"{self.star} - {self.corporation}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

