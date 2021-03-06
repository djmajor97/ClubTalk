# Generated by Django 2.0.4 on 2018-05-01 00:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0022_student_clubs_interested'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('positive', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])),
                ('hard', models.IntegerField(validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MinValueValidator(0)])),
                ('rating', models.IntegerField(default='0')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='page.Club')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='page.Student')),
            ],
        ),
    ]
