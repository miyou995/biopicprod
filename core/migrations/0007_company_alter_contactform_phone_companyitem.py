# Generated by Django 4.2.5 on 2024-06-02 13:36

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_about_service_description_alter_hiring_permis_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=25, null=True, verbose_name='Téléphone')),
                ('image_one', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image_detail_1')),
                ('order', models.IntegerField(blank=True, null=True, verbose_name='Display order')),
                ('image_two', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image_2')),
                ('about_one', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Text service')),
                ('about_two', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Page service ')),
            ],
        ),
        migrations.AlterField(
            model_name='contactform',
            name='phone',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Téléphone'),
        ),
        migrations.CreateModel(
            name='CompanyItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=180, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.company')),
            ],
        ),
    ]
