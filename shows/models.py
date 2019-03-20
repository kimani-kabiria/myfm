from django.db import models
from django.db.models.signals import pre_save
from myfm.utils import unique_sug_generator


class Station(models.Model):
    st_name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    st_icon = models.FileField()
    st_freq = models.CharField(max_length=100)
    st_live = models.CharField(max_length=1000)
    st_tagline = models.CharField(max_length=100)

    def __str__(self):
        return self.st_name + ' - ' + self.st_freq


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_sug_generator(instance, instance.st_name, instance.slug)


pre_save.connect(slug_save, sender=Station)


def get_absolute_url(self):
    return reverse("shows:stations", kwargs={"slug": self.slug})


class Show(models.Model):
    shw_title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    shw_hosts = models.CharField(max_length=250)
    shw_icon = models.FileField()
    shw_desc = models.CharField(max_length=1000, null='false')
    shw_station = models.ForeignKey(Station, on_delete=models.CASCADE)
    shw_live_on_time = models.TimeField(blank=True, null=True)
    shw_live_off_time = models.TimeField(blank=True, null=True)
    shw_days = models.CharField(max_length=250)

    def __str__(self):
        return self.shw_title + ' with - ' + self.shw_hosts


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_sug_generator(instance, instance.shw_title, instance.slug)


pre_save.connect(slug_save, sender=Show)


class Episode(models.Model):
    ep_show = models.ForeignKey(Show, on_delete=models.CASCADE)
    ep_title = models.CharField(max_length=250)
    ep_file = models.FileField()
    ep_release_date = models.DateField(blank=True, null=True, verbose_name="Release Date")

    def __str__(self):
        return self.ep_title
