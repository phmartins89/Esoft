from django.db import models
from datetime import datetime

# Create your models here.

class Endereco(models.Model):
    rua = models.CharField(max_length= 200)
    bairro = models.CharField(max_length= 200)
    numero = models.CharField(max_length= 10)
    complemento = models.CharField(max_length= 200)
    descricao = models.CharField(max_length= 200)
    cidade = models.CharField(max_length= 200)
    uf = models.CharField(max_length= 200)
    cep = models.CharField(max_length= 200)
    date_endereco = models.DateTimeField(default = datetime.now, blank= True)




                                       