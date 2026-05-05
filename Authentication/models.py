# ===============================================
# Data: 27/04/2026
# Autor: Pedro Teixeira Gontijo
# ===============================================

from django.db import models


class ApiClient(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    responsavel = models.CharField(max_length=100, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.responsavel

class ApiToken(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)

    cliente = models.ForeignKey(ApiClient, on_delete=models.CASCADE, related_name="tokens")
    ativo = models.BooleanField(default=True)

    prefix = models.CharField(max_length=12, blank=True)
    token_hash = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.cliente} - {self.prefix or 'sem-prefixo'}"