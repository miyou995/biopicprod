# Generated by Django 4.2.5 on 2024-07-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0018_rename_actif_slide_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slide',
            options={'ordering': ['ordering', '-id'], 'verbose_name': 'slide', 'verbose_name_plural': 'slides'},
        ),
        migrations.RenameField(
            model_name='slide',
            old_name='photo',
            new_name='image',
        ),
        migrations.AddField(
            model_name='slide',
            name='ordering',
            field=models.IntegerField(blank=True, null=True, verbose_name='Display order'),
        ),
        migrations.AddField(
            model_name='slide',
            name='placment',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Home About'), (2, 'About Page'), (3, 'Contact Page'), (4, 'Home Slider')], default=1, verbose_name='Slide emplacement'),
        ),
    ]
