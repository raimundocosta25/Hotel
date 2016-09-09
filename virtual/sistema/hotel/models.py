from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hotel(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    nomeContato = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    numQuartos = models.IntegerField()
    tipo = models.SmallIntegerField(choices=[(1, 'Pousada'), (2, 'Hotel'), (3, 'Albergue'), (4, 'Camping'), (5, 'Flat'), (6, 'Apartamento')])
    categoria = models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    checkin = models.DateField()
    checkout = models.DateField()
    Internet = models.BooleanField()

    def __str__(self):
        return '{0} - {1} - {2} - {3} - {4} - {5} - {6}'.format(self.nome, self.modelo, self.nomeContato, self.numero, self.endereco, self.checkin, self.checkout)

class Check(models.Model):
    checkin = models.DateField()
    checkout = models.DateField()

    def __str__(self):
        return '{0} - {1}'.format(self.checkin, self.checkout)

class Itens(models.Model):
    internet = models.BooleanField()
    breakfast = models.BooleanField()
    restaurante = models.BooleanField()
    lanchonete = models.BooleanField()
    lunch = models.BooleanField()
    piscina = models.BooleanField()
    sauna = models.BooleanField()
    academia = models.BooleanField()
    bicicleta = models.BooleanField()
    aluguelCarro = models.BooleanField()
    caixaEletronico = models.BooleanField()
    jardim = models.BooleanField()
    lougue = models.BooleanField()
    salaoJogos = models.BooleanField()
    capela = models.BooleanField()
    casaNoturna = models.BooleanField()
    parquinhoInfantio = models.BooleanField()
    lavanderia = models.BooleanField()
    engraxate = models.BooleanField()
    loja = models.BooleanField()
    barbeiro = models.BooleanField()
    estacionamento = models.BooleanField()
    bar = models.BooleanField()
    churrascaria = models.BooleanField()
    praia = models.BooleanField()
    banheiraHidro = models.BooleanField()
    servicoMassagem = models.BooleanField()
    cofre = models.BooleanField()
    terraco = models.BooleanField()
    biblioteca = models.BooleanField()
    karaoke = models.BooleanField()
    baba = models.BooleanField()
    servicoLimpeza = models.BooleanField()
    fax = models.BooleanField()
    auditorio = models.BooleanField()
    minimercado = models.BooleanField()

    def __str__(self):
        return self.internet

