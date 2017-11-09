from django.db import models


# Nossas classes irão simular nossas tabelas do DB
class Course(models.Model):
    # Ele gera a tabela como 1º parâmetro app_model (all in lowercase)
    name = models.CharField('Nome', max_length=100, unique=True)
    slug = models.SlugField('Atalho', primary_key=True)
    description = models.TextField('Descrição', blank=True)
    start_date = models.DateField(
        'Data de Início',
        null=True,  # A nível de banco de dados, ele pode ser nullable
        blank=True)  # Não obrigatório
    image = models.ImageField(
        upload_to='courses/images',
        verbose_name='Imagem',
        null=True, blank=True)
    created_at = models.DateTimeField(
        'Criado em',
        auto_now_add=True)  # Quando criar gera um date, não muda
    updated_at = models.DateTimeField(
        'Atualizado em',
        auto_now=True)  # Relativo, sempre muda de acordo com alterações

    class Meta:
        ordering = ['name']
        verbose_name = "curso"
        verbose_name_plural = "cursos"

    def __str__(self):
        return self.name
