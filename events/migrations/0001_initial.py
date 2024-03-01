# Generated by Django 3.2.24 on 2024-03-01 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=225)),
                ('event_date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('category', models.CharField(choices=[('Music', 'Music'), ('Electronic', 'Electronic'), ('Garage', 'Garage'), ('House', 'House'), ('DnB', 'DnB'), ('Hip-Hop', 'Hip-Hop'), ('Live-band', 'Live-band'), ('Soul/funk', 'Soul/funk')], default='Music', max_length=50)),
                ('image', models.ImageField(blank=True, default='../default_post_mpxuln', upload_to='images/')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]