from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Category(MPTTModel):

    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=("category name"),
        help_text=("francais : nom"),
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        unique=False,
        blank=False,
        verbose_name=("category safe URL"),
        help_text=(
            "francais : url"),
    )

    description = models.TextField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=("category description"),
        help_text=("francais : description"),
    )

    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=("parent of category"),
        help_text=("francais : parent"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = ("equipment category")
        verbose_name_plural = ("equipment categories")

class Equipment(models.Model):
    name = models.CharField(
        max_length=255,
        unique=False,
        null=True,
        blank=True,
        verbose_name=("equipment name"),
        help_text=("francais : nom"),
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        unique=False,
        blank=False,
        verbose_name=("equipment safe URL"),
        help_text=(
            "francais : url"),
    )
    categories = models.ManyToManyField(
        Category,
        null=True,
        unique=False,
        blank=True,
        verbose_name=("equipment categories"),
        help_text=(
            "francais : catégories"),
        )
    quantity = models.IntegerField(
        default=0,
        null=True,
        unique=False,
        blank=True,
        verbose_name=("equipment quantity"),
        help_text=(
            "francais : quantité"),
        )
