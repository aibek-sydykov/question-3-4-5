from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    body = models.TextField('Текст')
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, related_name='post_author')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('post.Post', models.CASCADE, related_name='post_comments')
    content = models.TextField('Текст')
    creation_date = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, 'comment_author')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.content

