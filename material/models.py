from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=100)  # nome
    type = models.CharField(max_length=100)  # tipo
    description = models.TextField()  # descricao
    thickness = models.DecimalField(max_digits=5, decimal_places=2)  # espessura
    width = models.DecimalField(max_digits=5, decimal_places=2)  # largura
    height = models.DecimalField(max_digits=5, decimal_places=2)  # altura
    color = models.CharField(max_length=50)  # cor
    manufacturer = models.CharField(max_length=100)  # fabricante
    manufacturer_code = models.CharField(max_length=50)  # codigo_fabricante
    price = models.DecimalField(max_digits=10, decimal_places=2)  # preco
    created_at = models.DateTimeField(auto_now_add=True)  # data_cadastro

    def __str__(self):
        return self.name
