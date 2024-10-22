# Generated by Django 2.1.3 on 2019-04-30 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PodEpisode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pod_ep_title', models.CharField(max_length=250)),
                ('pod_ep_desc', models.CharField(max_length=1000)),
                ('pod_ep_release', models.DateField(blank=True, null=True, verbose_name='Release Date')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PodShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pod_shw_title', models.CharField(max_length=250)),
                ('slug', models.SlugField(unique=True)),
                ('pod_shw_desc', models.CharField(max_length=1000)),
                ('pod_shw_host', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='podepisode',
            name='pod_ep_show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pods.PodShow'),
        ),
    ]
