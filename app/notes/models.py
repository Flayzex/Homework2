from django.contrib.auth import get_user_model
from django.db import models


class Notes(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name='Автор', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст заметки:')