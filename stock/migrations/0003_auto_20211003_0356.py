# Generated by Django 3.1.5 on 2021-10-03 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20211003_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]