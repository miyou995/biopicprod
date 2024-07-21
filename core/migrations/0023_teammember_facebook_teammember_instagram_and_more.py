# Generated by Django 4.2.5 on 2024-07-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_alter_service_options_service_ordering'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='Linkedin'),
        ),
    ]