# Generated by Django 4.2.1 on 2023-06-09 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
    ]
