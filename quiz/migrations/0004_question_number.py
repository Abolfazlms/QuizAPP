# Generated by Django 3.2.25 on 2024-06-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_rename_score_question_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]