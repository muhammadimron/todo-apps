# Generated by Django 4.2.7 on 2023-12-06 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_person_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
