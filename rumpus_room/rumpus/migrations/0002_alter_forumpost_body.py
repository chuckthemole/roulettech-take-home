# Generated by Django 5.0.7 on 2024-07-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rumpus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumpost',
            name='body',
            field=models.CharField(max_length=255),
        ),
    ]