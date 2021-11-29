from django.db import models


class Link(models.Model):
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылка"

    input_link = models.URLField(verbose_name='Ссылка')
    output_link = models.CharField(max_length=15, unique=True, blank=True, verbose_name='Короткая ссылка')
    clicks = models.PositiveIntegerField(blank=True, verbose_name='Количество переходов')
    date_create_link = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    date_last_click = models.DateTimeField(default=None, verbose_name='Дата последнего перехода')

    def __str__(self):
        return f' было {self.input_link} стало {self.output_link}'


