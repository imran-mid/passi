# Generated by Django 4.1.7 on 2023-03-03 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0037_alter_contact_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cause',
            name='total_price',
        ),
    ]
