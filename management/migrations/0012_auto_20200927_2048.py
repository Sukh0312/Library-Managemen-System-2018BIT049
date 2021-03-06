# Generated by Django 2.2 on 2020-09-27 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0011_auto_20200927_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=100, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='2', max_length=3),
        ),
    ]
