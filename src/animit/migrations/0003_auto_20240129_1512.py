# Generated by Django 3.1.4 on 2024-01-29 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animit', '0002_animal_animituser_animal_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='animituser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
