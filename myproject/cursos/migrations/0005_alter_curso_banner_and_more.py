# Generated by Django 5.2.1 on 2025-05-28 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0004_alter_curso_curso_encargado_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='banner',
            field=models.ImageField(upload_to='cursos/'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='curso_encargado_picture',
            field=models.ImageField(upload_to='cursos/encargado'),
        ),
    ]
