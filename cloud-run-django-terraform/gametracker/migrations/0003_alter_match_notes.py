# Generated by Django 3.2 on 2021-06-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gametracker', '0002_game_match_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='notes',
            field=models.TextField(default=None),
        ),
    ]
