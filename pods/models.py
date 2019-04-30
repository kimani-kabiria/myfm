from django.db import models
from django.db.models.signals import pre_save
from myfm.utils import unique_sug_generator
from django.conf import settings


class PodShow(models.Model):
    pod_shw_title = models.CharField(max_length=250)
    pod_shw_icon = models.FileField()
    pod_shw_host = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET(1))
    slug = models.SlugField(unique=True)
    pod_shw_desc = models.CharField(max_length=1000)


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_sug_generator(instance, instance.pod_shw_title, instance.slug)


pre_save.connect(slug_save, sender=PodShow)


class PodEpisode(models.Model):
    pod_ep_title = models.CharField(max_length=250)
    pod_ep_show = models.ForeignKey(PodShow, on_delete=models.CASCADE)
    pod_ep_file = models.FileField()
    pod_ep_desc = models.CharField(max_length=1000)
    pod_ep_release = models.DateField(blank=True, null=True, verbose_name="Release Date")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.pod_ep_show + ' : ' + self.pod_ep_title


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_sug_generator(instance, instance.pod_ep_title, instance.slug)


pre_save.connect(slug_save, sender=PodEpisode)


