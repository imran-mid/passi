# Generated by Django 4.1.7 on 2023-02-24 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pass', '0019_recentcause_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentcause',
            name='cause',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='pass.upcomingcause'),
            preserve_default=False,
        ),
    ]
