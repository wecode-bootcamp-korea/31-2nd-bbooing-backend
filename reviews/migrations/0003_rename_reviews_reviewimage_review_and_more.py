# Generated by Django 4.0.3 on 2022-04-14 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_reviewimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewimage',
            old_name='reviews',
            new_name='review',
        ),
        migrations.AlterModelTable(
            name='reviewimage',
            table='review_images',
        ),
    ]
