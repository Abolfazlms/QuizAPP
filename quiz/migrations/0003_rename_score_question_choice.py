# Generated by Django 3.2.25 on 2024-06-01 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_alter_question_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='score',
            new_name='choice',
        ),
    ]