# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-05-08 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0036_pt_br'),
        ('mod_stats_by_aircraft', '0005_fix_player_killboards_losses'),
    ]

    operations = [
        migrations.AddField(
            model_name='aircraftbucket',
            name='best_ak_in_sortie',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='best_ak_sortie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='stats.Sortie'),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='best_gk_in_sortie',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='best_gk_sortie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='stats.Sortie'),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='best_score_in_sortie',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='best_score_sortie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='stats.Sortie'),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='current_ak_streak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='current_gk_streak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='current_score_streak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='max_ak_streak',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='max_ak_streak_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='stats.Player'),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='max_gk_streak',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='max_gk_streak_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='stats.Player'),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='max_score_streak',
            field=models.IntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='aircraftbucket',
            name='max_score_streak_player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='stats.Player'),
        ),
        migrations.AddField(
            model_name='sortieaugmentation',
            name='computed_max_streaks',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='aircraftbucket',
            name='filter_type',
            field=models.CharField(choices=[('NO_FILTER', 'no filter'), ('NO_BOMBS_JUICE', 'no bombs nor juice'), ('BOMBS', 'bomb sorties only with no juice'), ('JUICE', 'juiced (upgraded engine/fuel)'), ('ALL', 'all')], db_index=True, default='NO_FILTER', max_length=16),
        ),
        migrations.AlterField(
            model_name='aircraftbucket',
            name='ground_kills',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='aircraftbucket',
            name='kills',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
    ]
