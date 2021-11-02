from django.db import models
from django.db.models import deletion

from base import enums

class Profile(models.Model):
    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    name = models.CharField('name', max_length=255)

class Post(models.Model):
    class Meta:
        verbose_name = 'social interaction'
        verbose_name_plural = 'social interactions'

    profile = models.ForeignKey('base.Profile', deletion.CASCADE, verbose_name='profile', related_name='posts')

    date = models.DateField('date')
    text = models.CharField('text', max_length=255)


class Comment(models.Model):
    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    post = models.ForeignKey('base.Post', deletion.CASCADE, verbose_name='post', related_name='comments')
    profile = models.ForeignKey('base.Profile', deletion.CASCADE, verbose_name='profile', related_name='comments')

    date = models.DateField('date')
    text = models.CharField('text', max_length=255)


class CommentReaction(models.Model):
    class Meta:
        verbose_name = 'comment reaction'
        verbose_name_plural = 'comment reactions'

    comment = models.ForeignKey('base.Comment', deletion.CASCADE, verbose_name='comment', related_name='reactions')
    profile = models.ForeignKey('base.Profile', deletion.CASCADE, verbose_name='profile', related_name='reactions')

    date = models.DateField('date')
    kind = models.CharField('kind', max_length=255, choices=enums.ReactionKind.to_choices())
