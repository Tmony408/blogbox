# Generated by Django 3.1.7 on 2021-04-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210406_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='video1',
            field=models.FileField(blank=True, null=True, upload_to='videos/%Y/%m/%d/'),
        ),
    ]
