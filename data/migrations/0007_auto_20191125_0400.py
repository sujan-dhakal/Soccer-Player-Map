# Generated by Django 2.0.7 on 2019-11-24 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20191125_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='college',
            name='College League',
            field=models.IntegerField(choices=[('0', 'Null'), ('1', 'America East Conference'), ('2', 'American Athletic Conference'), ('3', 'ASUN Conference'), ('4', 'Atlantic 10 Conference'), ('5', 'Atlantic Coast Conference'), ('6', 'Big East Conference'), ('7', 'Big South Conference'), ('8', 'Big Ten Conference'), ('9', 'Big West Conference'), ('10', 'Colonial Athletic Association'), ('11', 'Conference USA'), ('12', 'Horizon League'), ('13', 'Ivy League'), ('14', 'Metro Atlantic Athletic Conference'), ('15', 'Mid-American Conference'), ('16', 'Missouri Valley Conference'), ('17', 'Northeast Conference'), ('18', 'Pac-12 Conference'), ('19', 'Patriot League'), ('20', 'Southern Conference'), ('21', 'The Summit League'), ('22', 'Sun Belt Conference'), ('23', 'West Coast Conference'), ('24', 'Western Athletic Conference')]),
        ),
    ]
