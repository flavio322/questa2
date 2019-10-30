from django.db import models

class Tema(models.Model):
    nome=models.CharField(max_length=50)
    valor_aluguel = (
        ('Moeda', 'Moeda'),
        ('Cedula', 'Cedula'),
    )
    valor_aluguel = models.CharField(
        max_length=7,
        choices=valor_aluguel,
        default='Moeda',
    )
    cor_toalha=models.CharField(max_length=50)

class ItemTema(models.Model):
    nome = models.ForeignKey('Tema', on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)

class Endereco(models.Model):
    logradouro = models.CharField(max_length=50)
    numero = models.CharField(max_length=50)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    uf = models.CharField(max_length=50)
    cep = models.CharField(max_length=50)

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)

class Aluguel(models.Model):
    data_festa = models.DateField()
    hora_inicio = models.DecimalField( max_digits=5, decimal_places=2)
    hora_termino = models.DecimalField( max_digits=5, decimal_places=2)
    valor_cobroda = (
        ('Moeda', 'Moeda'),
        ('Cedula', 'Cedula'),
    )
    valor_cobrado = models.CharField(
        max_length=7,
        choices=valor_cobroda,
        default='Moeda',
    )
    nome_tema = models.ForeignKey('Tema', on_delete=models.CASCADE)
    endereco = models.OneToOneField('Endereco', on_delete=models.CASCADE)
    nome_cliente = models.OneToOneField(
        Cliente,
        on_delete=models.CASCADE
    )







# Create your models here.
