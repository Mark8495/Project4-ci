# Generated by Django 3.2.15 on 2022-09-16 21:06

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mealtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='breakfast', max_length=250, null=True, unique=True)),
                ('slug', models.SlugField(default='breakfast', max_length=250, null=True, unique=True)),
                ('mealtime_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='mealtime')),
            ],
        ),
        migrations.CreateModel(
            name='Preptime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preptime_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='preptime')),
                ('title', models.CharField(default='placeholder', max_length=250, null=True, unique=True)),
                ('slug', models.SlugField(default='placeholder', max_length=250, null=True, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='mealtime',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_posts', to='recipes.mealtime'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='preptime',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_posts', to='recipes.preptime'),
            preserve_default=False,
        ),
    ]
