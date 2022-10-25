from django.db import models
from django.db.models.fields import CharField

class Tema_Novo(models.Model):
    nome_tema = CharField(max_length=50)
    
    def __str__(self):
        return self.nome_tema
