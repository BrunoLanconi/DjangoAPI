# Generated by Django 3.1.3 on 2020-11-28 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshot', '0006_curso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_materia', models.IntegerField(null=True)),
                ('nome_materia', models.DateField(max_length=30, null=True)),
            ],
        ),
    ]
