# Generated by Django 5.1.3 on 2024-11-28 01:41

import core.models
import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_cliente_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={}, verbose_name='Imagem'),
        ),
    ]