from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Classificacao(models.Model):
    classificacao = models.CharField("Classificação", max_length=20)

    def __str__(self):
        return self.classificacao

    class Meta:
        ordering = ['id']
        verbose_name = 'Classificação'
        verbose_name_plural = 'Classificações'

class Viagem(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    data_inicio = models.DateTimeField("Início")
    data_fim = models.DateTimeField("Fim")
    classificacao = models.ForeignKey(Classificacao, on_delete=models.CASCADE, blank=True, null=True)
    nota = models.IntegerField("Nota", validators=[MaxValueValidator, MinValueValidator],
                               blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Viagem'
        verbose_name_plural = 'Viagens'
