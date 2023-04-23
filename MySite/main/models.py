from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post_type(models.Model):
    name = models.CharField("Название", max_length=255)
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.PROTECT)
    create = models.DateTimeField("Дата создания поста")
    published = models.DateTimeField("Дата публикации поста", blank=True)
    type_id = models.ForeignKey(Post_type, on_delete=models.PROTECT)
    title = models.CharField("Заголовок", max_length=255)
    content = models.TextField("Описание")
    img = models.URLField("Миниатюра поста", blank=True)
    price = models.IntegerField("Стоимость курса", blank=True)

    def __str__(self):
        return f"{self.type_id} - " \
               f"{self.title}"


class paid_curse(models.Model):
    post_ID = models.ForeignKey(Post, on_delete=models.PROTECT)
    price = models.IntegerField("Стоимость курса")

    def __str__(self):
        return f"{self.price} - " \
               f"{self.post_ID}"
