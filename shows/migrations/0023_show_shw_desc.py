# Generated by Django 2.1.2 on 2018-11-03 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0022_remove_show_shw_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='shw_desc',
            field=models.CharField(default='My Desc', max_length=1000),
        ),
    ]