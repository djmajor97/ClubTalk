# Generated by Django 2.0.4 on 2018-05-13 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0051_auto_20180513_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='website',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
