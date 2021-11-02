from base import enums
from base.models import Comment, CommentReaction, Post, Profile
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Create db initial data'

    def handle(self, *args, **options):
        admin_user = User.objects.filter(username='admin').first()
        if not admin_user:
            admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'adm')

        posts = []
        profiles = []
        for i in range(16):
            profile = Profile.objects.create(name=f'Profile {i}')
            profiles.append(profile)

            post = Post.objects.create(
                profile = profile,
                date    = timezone.now(),
                text    = f'Text from Post {i}')
            posts.append(post)

        for post in posts:
            for profile in profiles:
                comment = Comment.objects.create(
                    post    = post,
                    profile = profile,
                    date    = timezone.now(),
                    text    = f'Text from comment of {profile.name} in post of id {post.pk}')

                for _profile in profiles:
                    CommentReaction.objects.create(
                        comment = comment,
                        profile = _profile,
                        date    = timezone.now(),
                        kind    = enums.ReactionKind.LIKE.name)
