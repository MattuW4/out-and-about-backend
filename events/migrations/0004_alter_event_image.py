# Generated by Django 3.2.24 on 2024-03-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, default='../default_post_mpxuln', upload_to='images/'),
        ),
    ]
