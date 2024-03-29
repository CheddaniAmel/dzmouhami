# Generated by Django 5.0 on 2024-01-26 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avocat',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='avocat',
            name='langue',
            field=models.ManyToManyField(blank=True, default='frensh', to='app1.langue'),
        ),
        migrations.AlterField(
            model_name='avocat',
            name='numero_tlfn',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
