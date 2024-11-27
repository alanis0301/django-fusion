# Generated by Django 5.1.3 on 2024-11-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizada')),
                ('ativo', models.DateField(default=True, verbose_name='Ativo')),
                ('icone', models.CharField(choices=[('lni-log', 'Engrenagens'), ('lni-leaf', 'Folha'), ('lni-starts-up', 'Gráfica'), ('lni-rocket', 'Foguete'), ('lni-laptop-cellphone', 'Notecell'), ('lni-layers', 'Design')], max_length=100, verbose_name='Icone')),
                ('bio', models.TextField(max_length=200, verbose_name='Bio')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('posicao', models.CharField(choices=[('E', 'à esquerda'), ('D', 'à direita')], max_length=1, verbose_name='Posição')),
            ],
            options={
                'verbose_name': 'Feature',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.AlterModelOptions(
            name='funcionario',
            options={'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-log', 'Engrenagens'), ('lni-starts-up', 'Gráfica'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=100, verbose_name='Icone'),
        ),
    ]