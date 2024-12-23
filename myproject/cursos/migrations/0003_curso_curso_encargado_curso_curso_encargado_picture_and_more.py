# Generated by Django 5.1.3 on 2024-12-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_alter_curso_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='curso_encargado',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='curso_encargado_picture',
            field=models.ImageField(blank=True, default='alonso.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='curso',
            name='curso_lugares',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
