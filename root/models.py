from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from AxonNegarLanding import settings


class UseCase(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    icon = models.ImageField(upload_to='icons')

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='features/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    link_text = models.CharField(max_length=100, default="اطلاعات بیشتر دریافت کنید")
    link_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question


class Author(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Weblog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=200)
    slug = models.SlugField(unique=True, max_length=200, allow_unicode=True)
    what_you_read = models.TextField(verbose_name="What you read")
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    main_image = models.ImageField(upload_to='images/', blank=True, null=True)
    text = CKEditor5Field('Text', config_name='extends')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title