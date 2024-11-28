# Generated by Django 5.1.3 on 2024-11-27 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_feature_icone_alter_servico_icone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizada')),
                ('ativo', models.DateField(default=True, verbose_name='Ativo')),
                ('icone', models.CharField(choices=[('lni-package', 'Caixa'), ('lni-drop', 'Gota'), ('lni-star', 'Estrela')], max_length=100, verbose_name='Icone')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preco')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
            ],
            options={
                'verbose_name': 'Preco',
                'verbose_name_plural': 'Precos',
            },
        ),
    ]
