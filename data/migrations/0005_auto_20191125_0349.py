# Generated by Django 2.0.7 on 2019-11-24 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20191125_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='bio_link',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
