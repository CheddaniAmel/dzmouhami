# Generated by Django 5.0 on 2024-01-01 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_name_client_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='user_name',
            new_name='username',
        ),
    ]
