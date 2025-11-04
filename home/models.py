from django.db import models


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


from django.db import models

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.question
