# Generated by Django 2.0 on 2018-12-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_userbehavior_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='PersonalBlog',
            field=models.CharField(default='#', max_length=300, verbose_name='个人博客链接'),
        ),
    ]