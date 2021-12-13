from django.db import models


class Article(models.Model):
    title = models.CharField('Название статьи', max_length=100)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return f'Статья: {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.id}'


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete = models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)

class Shop(models.Model):
    shop_name = models.CharField('Название', max_length=250)
    address = models.CharField('Адрес', max_length=250)
    description = models.TextField('Описание услуг')

    def str(self):
        return self.shop_name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'