# Generated by Django 3.0.7 on 2021-01-28 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='media_url',
            field=models.CharField(default='media_url', max_length=1024),
            preserve_default=False,
        ),
    ]
