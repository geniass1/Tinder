# Generated by Django 3.1.5 on 2021-02-04 17:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20210204_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(default=datetime.datetime.now)),
                ('message', models.TextField()),
                ('who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_messages', to=settings.AUTH_USER_MODEL)),
                ('whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='whom_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
