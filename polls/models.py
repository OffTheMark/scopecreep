from datetime import datetime

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class SuggestionBox(models.Model):
    owner = models.ForeignKey(
        User,
        null=True
    )
    description = models.TextField(
        blank=True
    )
    date_created = models.DateTimeField(
        default=datetime.now
    )


class Suggestion(models.Model):
    suggestion_box = models.ForeignKey(
        SuggestionBox,
        on_delete=models.CASCADE
    )
    description = models.TextField(
        blank=True
    )
    date_created = models.DateTimeField(
        default=datetime.now
    )

    def score(self):
        return sum([vote.opinion for vote in self.vote_set.all()])


class Comment(models.Model):
    suggestion = models.ForeignKey(
        Suggestion,
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        default=datetime.now
    )


class Vote(models.Model):
    suggestion = models.ForeignKey(
        Suggestion,
        on_delete=models.CASCADE
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
