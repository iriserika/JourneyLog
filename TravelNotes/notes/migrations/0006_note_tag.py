# Generated by Django 2.0.7 on 2019-12-01 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20191130_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tag',
            field=models.CharField(default='Weekend Break', max_length=20),
        ),
    ]