# Generated by Django 3.1.8 on 2021-08-31 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='vaccines',
            field=models.ManyToManyField(to='base.Vaccine', verbose_name='vacinas'),
        ),
    ]
