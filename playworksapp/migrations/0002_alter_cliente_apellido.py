# Generated by Django 5.0.7 on 2024-07-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playworksapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=40),
        ),
    ]
