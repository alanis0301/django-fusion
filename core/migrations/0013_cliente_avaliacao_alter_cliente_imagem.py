# Generated by Django 5.1.3 on 2024-11-28 02:02

import core.models
import django.core.validators
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_cliente_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='avaliacao',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)], verbose_name='Avaliacao'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 200, 'width': 200}}, verbose_name='Imagem'),
        ),
    ]
