# Generated by Django 5.1.3 on 2024-11-27 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_feature_alter_funcionario_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagens'), ('lni-leaf', 'Folha'), ('lni-stats-up', 'Gráfica'), ('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Notecell'), ('lni-layers', 'Design')], max_length=100, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagens'), ('lni-stats-up', 'Gráfica'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=100, verbose_name='Icone'),
        ),
    ]
