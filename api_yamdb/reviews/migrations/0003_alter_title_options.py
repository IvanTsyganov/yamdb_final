# Generated by Django 3.2.18 on 2023-05-03 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('name',)},
        ),
    ]
