# Generated by Django 4.2.1 on 2023-06-12 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='numero_legajo',
            field=models.PositiveIntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
