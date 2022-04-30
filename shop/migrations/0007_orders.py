# Generated by Django 4.0.3 on 2022-04-20 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_emaol_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('state', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=180)),
                ('zip_code', models.CharField(max_length=80)),
            ],
        ),
    ]
