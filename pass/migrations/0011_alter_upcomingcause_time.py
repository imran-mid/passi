# Generated by Django 4.1.7 on 2023-02-23 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0010_alter_upcomingcause_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upcomingcause',
            name='time',
            field=models.DateTimeField(),
        ),
    ]
