# Generated by Django 2.0.4 on 2018-05-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0025_auto_20180501_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='clubs_interested',
            field=models.ManyToManyField(blank=True, null=True, related_name='interested', to='page.Club'),
        ),
    ]