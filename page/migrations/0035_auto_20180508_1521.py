# Generated by Django 2.0.4 on 2018-05-08 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0034_auto_20180508_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='category',
            field=models.ManyToManyField(blank=True, to='page.Category'),
        ),
    ]
