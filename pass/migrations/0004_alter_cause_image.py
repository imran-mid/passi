# Generated by Django 4.1.7 on 2023-02-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0003_cause_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]