# Generated by Django 5.1.3 on 2024-12-12 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_user_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.TextField(max_length=200)),
                ('message', models.TextField(max_length=400)),
            ],
        ),
    ]
