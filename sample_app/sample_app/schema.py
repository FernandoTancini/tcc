from django.db.models.expressions import OuterRef, Subquery
import graphene
from graphene.types.schema import Schema
from base.models import Comment, CommentReaction, Post, Profile
from graphene_django.debug import DjangoDebug
from graphene_django.schema import DjangoSchema
from graphene_django.types import DjangoObjectType
from base.controllers import annotate_is_bully

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

    is_from_bully = graphene.Boolean()

    # def resolve_is_from_bully(root, info):
    #     profile_qs = Profile.objects.filter(pk=root.profile_id)
    #     is_from_bully = annotate_is_bully(profile_qs).first().is_bully

    #     return is_from_bully

    def annotate_is_from_bully(root_queryset, info):
        profile_qs = Profile.objects.filter(pk=OuterRef('profile'))
        is_from_bully = annotate_is_bully(profile_qs).values('is_bully')

        return root_queryset.annotate(is_from_bully=Subquery(is_from_bully))


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")
    feed_posts = graphene.List(
        PostType,
        offset=graphene.Int(required=True),
        limit=graphene.Int(required=True))

    def resolve_feed_posts(root, info, offset, limit):
        return Post.objects.all()[offset:limit]


# schema = Schema(query=Query)
schema = DjangoSchema(query=Query, automatic_preparation=True)
