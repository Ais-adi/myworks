# Generated by Django 3.2.15 on 2022-12-17 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytodoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1999-04-26'),
            preserve_default=False,
        ),
    ]
