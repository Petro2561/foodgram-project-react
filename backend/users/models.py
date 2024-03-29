from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=254,
        verbose_name='Почта',
        unique=True,
        error_messages={
            "unique": "Пользователь с такой почтой уже существует",
        },
    )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
    )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
    )
    username = models.CharField(
        verbose_name="Имя пользователя",
        max_length=150,
        unique=True,
        help_text=(
            "Введите уникальное имя пользователя. Максимум 150 символов. "
            "Используйте только английские буквы, цифры и символы @/./+/-/_"
        ),
        error_messages={
            "unique": "Пользователь с таким именем уже существует",
        },
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    follower = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='subscribing',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return f'{self.follower} подписался на {self.following}'


