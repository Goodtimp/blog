# Generated by Django 2.0 on 2018-11-06 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xadmin', '0003_auto_20160715_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='query',
            field=models.CharField(blank=True, max_length=1000, verbose_name='Query String'),
        ),
    ]