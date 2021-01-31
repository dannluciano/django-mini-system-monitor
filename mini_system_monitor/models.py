from django.db import models


class Settings(models.Model):
    class Meta:
        verbose_name = "Setting"
        verbose_name_plural = "Settings"


class Env(models.Model):
    class Meta:
        verbose_name = "Env"
        verbose_name_plural = "Envs"


class Overview(models.Model):
    class Meta:
        verbose_name = " Overview"
        verbose_name_plural = " Overview"
