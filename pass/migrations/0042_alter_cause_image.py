# Generated by Django 4.1.7 on 2023-03-04 20:05

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0041_alter_cause_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[50, 41], upload_to='media'),
        ),
    ]