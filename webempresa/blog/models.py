from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

#Class model Category
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name

#Class model Post
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="título")
    content = models.TextField(verbose_name="contenido")
    published = models.DateField(verbose_name="fecha de publicación", default=now)
    image = models.ImageField(verbose_name="imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="categorias", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title