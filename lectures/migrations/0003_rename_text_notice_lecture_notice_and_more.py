# Generated by Django 4.0.3 on 2022-04-14 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_lecture_text_notice_lecture_text_recommendation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='text_notice',
            new_name='notice',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='text_recommendation',
            new_name='recommendation',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='text_summary',
            new_name='summary',
        ),
    ]
