# Generated by Django 3.1.5 on 2021-01-31 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_system_monitor', '0002_overview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
        ),
    ]
