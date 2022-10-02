import datetime
from exiffield.fields import ExifField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Дата создания')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.question_text

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

        

class Albums(models.Model):
    external_id = models.PositiveIntegerField(verbose_name = "Album ID", null=True)
    is_public = models.BooleanField(default=True)
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True)
    view_count = models.PositiveIntegerField(("Число просмотров"), default=0, editable=False)
    preview = models.ImageField(upload_to='gallery/data/previews/')
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    last_updated = models.DateTimeField(verbose_name='Дата изменения')
    # creator = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, null=False, blank=False,
    #     verbose_name='Creator', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Photos(models.Model):
    external_id = models.PositiveIntegerField(verbose_name="Photo ID", null=True)
    image = models.ImageField(upload_to='gallery/data/images/')
    exif = ExifField(
        source='image',
    )
    note = models.CharField(max_length=200)
    albums = models.ForeignKey(Albums, on_delete = models.PROTECT)
    create_date = models.DateTimeField(verbose_name='Дата добавления')
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.note


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choise_text
