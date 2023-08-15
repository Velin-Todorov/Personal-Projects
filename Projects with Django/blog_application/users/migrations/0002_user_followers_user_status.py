# Generated by Django 4.2.1 on 2023-06-09 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=2),
        ),
    ]