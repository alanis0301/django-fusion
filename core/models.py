import uuid

from django.db import models

from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualizada', auto_now=True)
    ativo = models.DateField('Ativo', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog','Engrenagens'),
        ('lni-stats-up', 'Gráfica'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket','Foguete'),
    )
    servico = models.CharField('Servico', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=100, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'

    def __str__(self):
        return self.servico

class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width':480, 'height':480, 'crop': True}})
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome

class Feature(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagens'),
        ('lni-leaf', 'Folha'),
        ('lni-stats-up', 'Gráfica'),
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Notecell'),
        ('lni-layers', 'Design'),
    )

    POSICAO_CHOICES = (
        ('E', 'à esquerda'),
        ('D', 'à direita'),
    )

    icone = models.CharField('Icone', max_length=100, choices=ICONE_CHOICES)
    bio = models.TextField('Bio', max_length=200)
    nome = models.CharField('Nome', max_length=100)
    posicao = models.CharField('Posição', max_length=1, choices=POSICAO_CHOICES)
    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'

    def __str__(self):
        return self.nome
