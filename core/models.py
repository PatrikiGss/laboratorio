from django.db import models

class genero(models.Model):
    genero=models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        """representação em string do modelo"""
        return str(self.genero)

class livros(models.Model):
    """"livros cadastrados pelo usuario"""
    genero=models.ManyToManyField(genero)
    livro= models.CharField(max_length=50)
    descrição=models.CharField(max_length=500)
    autor=models.CharField(max_length=50)
    quant=models.PositiveIntegerField()
    hora_cadastro=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """representação em string do modelo"""
        return str(self.livro)
    #
    
    