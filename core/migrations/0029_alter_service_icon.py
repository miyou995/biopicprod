# Generated by Django 4.2.5 on 2024-07-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_portfolioitem_display_on_home_service_icon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='images/', verbose_name='icon'),
        ),
    ]
