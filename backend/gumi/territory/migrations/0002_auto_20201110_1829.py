# Generated by Django 2.2.16 on 2020-11-10 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('territory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='Territory',
            new_name='territory',
        ),
    ]
