# Generated by Django 3.2.7 on 2021-09-24 23:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_deepthought_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deepthought',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]