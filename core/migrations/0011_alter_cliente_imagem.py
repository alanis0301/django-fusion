# Generated by Django 5.1.3 on 2024-11-28 01:33

import core.models
import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_cliente_imagem_alter_cliente_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 200, 'width': 200}}, verbose_name='Imagem'),
        ),
    ]
