# Generated by Django 5.0 on 2023-12-30 04:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avocat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('adresse', models.TextField()),
                ('numero_tlfn', models.CharField(max_length=20)),
                ('specialisation', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('categories', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('numero_tlfn', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texte', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('avocat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.avocat')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.client')),
            ],
        ),
        migrations.CreateModel(
            name='ProfilAvocat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.TextField()),
                ('rating', models.FloatField()),
                ('site_web', models.URLField(blank=True, null=True)),
                ('avocat', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.avocat')),
                ('blogs', models.ManyToManyField(blank=True, related_name='profils_avocats', to='app1.blog')),
            ],
        ),
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('avocat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.avocat')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.client')),
            ],
        ),
    ]
