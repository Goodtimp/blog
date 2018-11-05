# Generated by Django 2.0 on 2018-10-31 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_articlesuggests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aritcledatils',
            name='LastDataChange',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='最后修改时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='ArticleSuggests',
            field=models.CharField(max_length=500, null=True, verbose_name='文章详情'),
        ),
        migrations.AlterField(
            model_name='article',
            name='PostedTime',
            field=models.DateTimeField(default=datetime.date.today, verbose_name='发表时间'),
        ),
    ]