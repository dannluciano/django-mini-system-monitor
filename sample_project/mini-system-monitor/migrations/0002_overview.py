# Generated by Django 3.1.5 on 2021-01-29 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini-system-monitor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Overview',
                'verbose_name_plural': 'Overview',
            },
        ),
    ]
