# Generated by Django 3.2.7 on 2021-09-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_deepthought_deepthought_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='deepthought',
            name='url',
            field=models.SlugField(blank=True, editable=False, max_length=500, unique=True),
        ),
    ]
