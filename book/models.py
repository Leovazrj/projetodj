from django.db import models

class Book(models.Model):
    nome = models.CharField(verbose_name= 'Nome do Livro', max_length=150, null=False, blank=False)
    genero = models.CharField(verbose_name='Gênero', max_length= 100, null=False, blank=False)  
    idioma = models.CharField(verbose_name='Idioma', max_length=50, null=True, blank=True)
    escritor = models.CharField(verbose_name='Escritor(a):', max_length=150, null=False, blank=False)
    sinopse = models.CharField(verbose_name='Sinopse', max_length=500, null=True, blank=True)
    observacao = models.CharField(verbose_name='Observação', max_length=150, null=True, blank=True)
    compra = models.FloatField(verbose_name='Preço de compra', max_length=15 , null=False, blank=False)
    venda = models.FloatField(verbose_name='Preço de venda', max_length=15, null=False, blank=False)
    data_compra = models.DateField(verbose_name='Data da compra', auto_now=False)
    data_venda = models.DateField(verbose_name='Data da venda', auto_now=False)
    imagem = models.ImageField(verbose_name='Imagen', null=True, blank=True, upload_to='media/%Y/%m/%d')
    
    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        
    def __str__(self): 
        return self.name    
    
