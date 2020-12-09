# Generated by Django 2.2 on 2020-09-26 06:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_sms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='return_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]