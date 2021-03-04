# Generated by Django 3.1.6 on 2021-02-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smashbotspain', '0003_player_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arenaplayer',
            name='status',
            field=models.CharField(choices=[('WAITING', 'Waiting'), ('PLAYING', 'Playing'), ('GGS', 'GGs'), ('INVITED', 'Invited')], max_length=7),
        ),
    ]
