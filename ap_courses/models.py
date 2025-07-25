from django.db import models

from stdimage import StdImageField

import uuid

from django.template.defaultfilters import slugify

from django.db.models import signals

import utils

def get_file_path(_instance, file_name):
    extension = file_name.split('.')[1]
    file_name = f'images_courses/{_instance.name}/{uuid.uuid4()}.{extension}'
    return file_name

def get_file_path_video(_instance, file_name):
    extension = file_name.split('.')[1]
    file_name = f'videos_courses/{_instance.name}/{uuid.uuid4()}.{extension}'
    return file_name


class Category(models.Model):
    name = models.CharField('Nome da Categoria', max_length=100)
    slug = models.SlugField('Slug', max_length=500, editable=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class SubCategory(models.Model):
    name = models.CharField('Nome sub-Categoria', max_length=100)
    slug = models.SlugField('Slug', max_length=500, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'SubCategoria'
        verbose_name = 'SubCategoria'
        verbose_name_plural = 'SubCategorias'


class Course(models.Model):
    name = models.CharField('Nome', max_length=100)
    video = models.FileField('Video', upload_to=get_file_path_video)
    description_short = models.CharField('Descrição', max_length=500)
    detailed_description = models.TextField('Descrição detalhada')
    news = models.BooleanField('Novidade?')
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    level = models.CharField('Nível', max_length=100)
    slug = models.SlugField('Slug', max_length=500, editable=False)
    image = StdImageField('Imagem', upload_to=get_file_path, variations={'thumbnail': {'width': 150, 'height': 150, 'crop': True}})
    name_teacher = models.CharField('Nome do Professor', max_length=100)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.name
    

class ClassRoom(models.Model):
    name = models.TextField('Nome', max_length=100)

    class Meta:
        db_table = 'Aula'
        verbose_name = 'Aula'
        verbose_name_plural = 'Aulas'

    def __str__(self):
        return self.name
    

class Section(models.Model):
    name = models.CharField('Nome da Seção', max_length=100)
    classes_room = models.ManyToManyField(ClassRoom, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Seção'
        verbose_name = 'Seção'
        verbose_name_plural = 'Seções'

    def __str__(self):
        return self.name
    

def pre_save_model(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(pre_save_model, sender=Course)

signals.pre_save.connect(pre_save_model, sender=Category)

signals.pre_save.connect(pre_save_model, sender=SubCategory)
