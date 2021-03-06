# Generated by Django 3.1 on 2020-08-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('wdate', models.DateTimeField(verbose_name='작성일')),
                ('writer', models.CharField(max_length=50, verbose_name='작성자')),
                ('hit', models.IntegerField(verbose_name='조회수')),
            ],
        ),
    ]
