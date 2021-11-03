from django.db.models import Count, OuterRef
from django.db.models.expressions import Case, When
from django.db.models.fields import BooleanField

from base import enums
from base.expressions import SubqueryAgg
from base.models import CommentReaction


def annotate_is_bully(profile_qs):
    reactions = CommentReaction.objects.filter(profile=OuterRef('pk'))
    hate_reactions = reactions.filter(kind=enums.ReactionKind.HATE.name)
    hate_ratio_exp = SubqueryAgg(hate_reactions, Count('pk')) / SubqueryAgg(reactions, Count('pk'))

    return profile_qs \
        .annotate(
            _hate_ratio=hate_ratio_exp,
            is_bully=Case(
                When(_hate_ratio__gt=0.5, then=True),
                default=False,
                output_field=BooleanField()))
