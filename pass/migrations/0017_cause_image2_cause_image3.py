# Generated by Django 4.1.7 on 2023-02-24 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0016_alter_cause_cause'),
    ]

    operations = [
        migrations.AddField(
            model_name='cause',
            name='image2',
            field=models.ImageField(blank=True, default='media/causes2.jpg', upload_to='media'),
        ),
        migrations.AddField(
            model_name='cause',
            name='image3',
            field=models.ImageField(blank=True, default='media/causes3.jpg', upload_to='media'),
        ),
    ]