# Generated by Django 4.2.7 on 2023-12-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.CharField(default='Admin', max_length=255, verbose_name='Role'),
        ),
    ]
