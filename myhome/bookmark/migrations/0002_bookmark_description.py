# Generated by Django 3.1 on 2020-08-14 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='description',
            field=models.CharField(blank=True, max_length=100, verbose_name='DESCRIPTION'),
        ),
    ]
