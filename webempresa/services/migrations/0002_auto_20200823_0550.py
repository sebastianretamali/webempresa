# Generated by Django 2.2.2 on 2020-08-23 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Project',
            new_name='Service',
        ),
        migrations.AlterModelOptions(
            name='service',
            options={},
        ),
    ]