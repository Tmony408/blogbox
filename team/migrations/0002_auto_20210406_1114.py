# Generated by Django 3.1.7 on 2021-04-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='is_mvp',
            field=models.BooleanField(default=False),
        ),
    ]
