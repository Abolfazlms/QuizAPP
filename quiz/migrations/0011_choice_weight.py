# Generated by Django 3.2.25 on 2024-06-19 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0010_auto_20240619_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='weight',
            field=models.FloatField(default=1.0),
        ),
    ]
