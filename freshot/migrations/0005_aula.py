# Generated by Django 3.1.3 on 2020-11-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freshot', '0004_auto_20201128_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_aula', models.IntegerField(null=True)),
                ('semestre', models.IntegerField(null=True)),
            ],
        ),
    ]