# Generated by Django 4.1.3 on 2022-11-29 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0002_libro_likes_alter_libro_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='descripcion',
            field=models.CharField(default='-', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libro',
            name='estado',
            field=models.CharField(choices=[('N', 'No Disponible'), ('P', 'En prestamo'), ('D', 'Disponible')], max_length=1),
        ),
    ]