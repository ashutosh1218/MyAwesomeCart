# Generated by Django 4.0.3 on 2022-04-16 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='emaol',
            new_name='email',
        ),
    ]
