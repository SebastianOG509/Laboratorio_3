# Generated by Django 4.1.3 on 2022-11-30 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libros', '0005_alter_libro_estado_alter_libro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='estado',
            field=models.CharField(choices=[('D', 'Disponible'), ('N', 'No Disponible'), ('P', 'En prestamo')], max_length=1),
        ),
    ]
