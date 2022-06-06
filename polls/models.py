import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.template.defaultfilters import slugify


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class DeepThought(models.Model):
    deepThought_title = models.CharField(max_length=200)
    deepThought_text = models.CharField(max_length=300)
    pub_date = models.DateField(default=timezone.now)
    url = models.SlugField(max_length=500, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.url = slugify(self.deepThought_title)
        super(DeepThought, self).save(*args, **kwargs)

    def __str__(self):
        return self.deepThought_title + ": " + self.deepThought_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
