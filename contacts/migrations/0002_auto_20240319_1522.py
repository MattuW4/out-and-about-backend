# Generated by Django 3.2.24 on 2024-03-19 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='content',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='reason',
        ),
    ]
