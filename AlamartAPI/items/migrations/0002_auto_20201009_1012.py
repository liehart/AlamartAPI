# Generated by Django 3.1.2 on 2020-10-09 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maker',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
