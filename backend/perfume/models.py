from django.db import models
from django.utils.text import slugify


class Aroma(models.Model):
    name = models.CharField('Название аромата', max_length=64)

    class Meta:
        verbose_name = 'Аромат'
        verbose_name_plural = 'Ароматы'
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name


class Vendor(models.Model):
    name = models.CharField('Название', max_length=64)
    url = models.URLField('Ссылка', max_length=200, unique=True)
    logo = models.ImageField(verbose_name='Лого')

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Perfume(models.Model):
    m = 'M'
    f = 'F'
    SEXES = {
        (m, 'мужской'),
        (f, 'женский'),
    }

    TYPE_CHOICES = (
        ('EDT', 'Туалетная вода'),
        ('EDP', 'Парфюмерная вода'),
        ('ES', 'Одеколон'),
        ('PARFUM', 'Духи'),
        ('EF', 'Вода (Eau Fraiche)'),
    )

    name = models.CharField('Название', max_length=64)
    description = models.TextField('Описание')
    volume = models.PositiveSmallIntegerField('Объем')
    image = models.ImageField(verbose_name='Картинка')
    sex = models.CharField('Пол', max_length=1, choices=SEXES)
    type = models.CharField(
        'Тип продукта', max_length=10, choices=TYPE_CHOICES
    )
    vendors = models.ManyToManyField(Vendor, through='PerfumeVendor')
    aromas = models.ManyToManyField(Aroma, through='PerfumeAroma')

    class Meta:
        verbose_name = 'Парфюм'
        verbose_name_plural = 'Парфюм'

    def __str__(self) -> str:
        return self.name


class PerfumeVendor(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    evaluation = models.DecimalField('Оценка', max_digits=2, decimal_places=1)
    url_to_perfume = models.URLField('Ссылка на продукт')

    class Meta:
        verbose_name = 'Продукт - продавец'
        verbose_name_plural = 'Продукты - продавцы'

    def __str__(self) -> str:
        return f'{self.perfume.name} - {self.vendor.name}'


class PerfumeAroma(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE)
    aroma = models.ForeignKey(Aroma, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Парфюм - аромат'
        verbose_name_plural = 'Парфюм - ароматы'

    def __str__(self) -> str:
        return f'{self.perfume.name} - {self.aroma.name}'
