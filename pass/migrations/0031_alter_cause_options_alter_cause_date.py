# Generated by Django 4.1.7 on 2023-02-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0030_alter_cause_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cause',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='cause',
            name='date',
            field=models.DateField(),
        ),
    ]
