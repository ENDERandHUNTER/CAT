# Generated by Django 5.0.4 on 2024-04-28 10:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usersignin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialdatatable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_text', models.TextField()),
                ('target_text', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersignin.user')),
            ],
        ),
    ]
