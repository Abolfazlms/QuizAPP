# Generated by Django 3.2.25 on 2024-06-01 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['category']},
        ),
    ]
