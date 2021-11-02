import graphene
from base.models import Comment, CommentReaction, Post, Profile
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg
from graphene_django.debug import DjangoDebug
from graphene_django.schema import DjangoSchema
from graphene_django.types import DjangoObjectType


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ['name']


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ['date', 'text', 'profile', 'comments']


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ['date', 'text', 'profile', 'reactions']


class CommentReactionType(DjangoObjectType):
    class Meta:
        model = CommentReaction
        fields = ['date', 'kind', 'profile']


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")
    feed_posts = graphene.List(
        PostType,
        offset=graphene.Int(required=True),
        limit=graphene.Int(required=True))

    def resolve_feed_posts(root, info, offset, limit):
        return Post.objects.all()[offset:limit]


schema = DjangoSchema(query=Query, automatic_preparation=False)
