from django.db import models


class Env(models.Model):

    name = models.CharField(
        "name",
        editable=False,
        max_length=255
    )

    value = models.CharField(
        "value",
        editable=False,
        max_length=512
    )

    class Meta:
        verbose_name = "Env"
        verbose_name_plural = "Envs"


class Overview(models.Model):
    class Meta:
        verbose_name = "Overview"
        verbose_name_plural = "Overview"
