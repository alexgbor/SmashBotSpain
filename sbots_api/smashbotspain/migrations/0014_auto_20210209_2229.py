# Generated by Django 3.1.6 on 2021-02-09 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smashbotspain', '0013_tier_channel_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arena',
            name='tier',
        ),
        migrations.AddField(
            model_name='arena',
            name='max_tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='max_tier', to='smashbotspain.tier'),
        ),
        migrations.AddField(
            model_name='arena',
            name='min_tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='min_tier', to='smashbotspain.tier'),
        ),
    ]
