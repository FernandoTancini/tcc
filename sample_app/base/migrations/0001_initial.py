# Generated by Django 3.1.8 on 2021-11-02 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('text', models.CharField(max_length=255, verbose_name='text')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('text', models.CharField(max_length=255, verbose_name='text')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='base.profile')),
            ],
            options={
                'verbose_name': 'social interaction',
                'verbose_name_plural': 'social interactions',
            },
        ),
        migrations.CreateModel(
            name='CommentReaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('kind', models.CharField(choices=[('LIKE', 'LIKE'), ('LOVE', 'LOVE'), ('HATE', 'HATE')], max_length=255, verbose_name='kind')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='base.comment')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='base.profile')),
            ],
            options={
                'verbose_name': 'comment reaction',
                'verbose_name_plural': 'comment reactions',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='base.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='base.profile'),
        ),
    ]
