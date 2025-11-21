from django.conf.global_settings import AUTH_USER_MODEL
from django.core.validators import RegexValidator
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from AxonNegarLanding import settings
from root.upload_path_utilities import get_upload_path


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


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Weblog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=200)
    slug = models.SlugField(unique=True, max_length=200, allow_unicode=True)
    tags = models.ManyToManyField(Tag)
    what_you_read = models.TextField(verbose_name="What you read")
    cover_image = models.ImageField(upload_to='covers/', help_text="570x300")
    main_image = models.ImageField(upload_to='images/', help_text="620x300")
    text = CKEditor5Field('Text', config_name='extends')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    mobile_regex = RegexValidator(
        regex=r'^09\d{9}$',
        message="Phone number must be entered in the format: '09xxxxxxxxx'. Up to 11 digits allowed."
    )

    name = models.CharField("Full Name", max_length=100)
    email = models.EmailField("Email Address")
    phone = models.CharField("Phone Number", max_length=20, validators=[mobile_regex])
    website = models.URLField("Website", blank=True, null=True)
    message = models.TextField("Message")
    created_at = models.DateTimeField("Received at", auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


class Release(models.Model):
    class OperatingSystem(models.TextChoices):
        WINDOWS = 'windows', 'Windows'
        MACOS = 'macos', 'macOS'
        LINUX_DEB = 'linux_deb', 'Linux (Debian/Ubuntu)'
        LINUX_RPM = 'linux_rpm', 'Linux (Fedora/Red Hat)'
        ANDROID = 'android', 'Android'

    version = models.CharField(max_length=20, help_text="e.g., v1.0.1")
    os = models.CharField(
        max_length=20,
        choices=OperatingSystem.choices,
        help_text="The target operating system for this file."
    )
    notes = models.TextField(blank=True, help_text="Release notes or a short description.")
    release_file = models.FileField(upload_to=get_upload_path)
    upload_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('version', 'os')
        get_latest_by = 'upload_date'

    def __str__(self):
        return f"Release {self.version} for {self.get_os_display()}"
