# Generated by Django 3.0.8 on 2021-01-15 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_destinationcompany_d_sm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destinationcompany',
            old_name='d_sm',
            new_name='dsm',
        ),
    ]
