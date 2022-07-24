# Generated by Django 4.0.6 on 2022-07-21 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_coder', '0002_estudiante_rename_nombre_curso_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_entrega', models.DateField()),
                ('Entregado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('profesion', models.CharField(max_length=50)),
            ],
        ),
    ]