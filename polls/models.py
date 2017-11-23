from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Topic(models.Model):
    submitter = models.ForeignKey(
        User,
        null=True
    )
    name = models.TextField(
        blank=False,
        null=False,
        default=""
    )
    description = models.TextField(
        blank=True
    )
    date_created = models.DateTimeField(
        default=datetime.now
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-date_created"]


class Suggestion(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE
    )
    submitter = models.ForeignKey(
        User,
        null=True
    )
    name = models.TextField(
        blank=False,
        null=False,
        default=""
    )
    description = models.TextField(
        blank=True
    )
    date_created = models.DateTimeField(
        default=datetime.now
    )

    def score(self):
        return sum([vote.opinion for vote in self.vote_set.all()])

    def __str__(self):
        return self.name


class Comment(models.Model):
    suggestion = models.ForeignKey(
        Suggestion,
        on_delete=models.CASCADE
    )
    submitter = models.ForeignKey(
        User,
        null=True
    )
    text = models.TextField(
        blank=False,
        null=False,
        default=""
    )
    date_created = models.DateTimeField(
        default=datetime.now
    )

    def __str__(self):
        return self.text


class Vote(models.Model):
    suggestion = models.ForeignKey(
        Suggestion,
        on_delete=models.CASCADE
    )
    submitter = models.ForeignKey(
        User,
        null=True
    )
    opinion = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(-1),
            MaxValueValidator(1)
        ]
    )
    date_created = models.DateTimeField(
        default=datetime.now
    )

    def __str__(self):
        return "Vote {} for {} by {}".format(self.opinion, self.suggestion, self.submitter)
