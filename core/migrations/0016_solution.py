# Generated by Django 4.2.5 on 2024-07-11 10:40

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_company_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nom de la solution')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=70, verbose_name='Grand titre de la solution')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/solutions', verbose_name='Petite image')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='images/solutions', verbose_name='Grande image')),
                ('text', models.TextField(blank=True, null=True, verbose_name='petit texte')),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Description du service')),
            ],
        ),
    ]