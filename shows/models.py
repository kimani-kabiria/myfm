from django.db import models
from datetime import date, time


class Station(models.Model):
    st_name = models.CharField(max_length=250)
    st_icon = models.CharField(max_length=1000)
    st_freq = models.CharField(max_length=100)

    def __str__(self):
        return self.st_name + ' - ' + self.st_freq


class Show(models.Model):
    shw_title = models.CharField(max_length=250)
    shw_hosts = models.CharField(max_length=250)
    shw_icon = models.CharField(max_length=1000)
    shw_desc = models.CharField(max_length=1000, null='false')
    shw_station = models.ForeignKey(Station, on_delete=models.CASCADE)
    shw_live_on_time = models.TimeField(blank=True, null=True)
    shw_live_off_time = models.TimeField(blank=True, null=True)

    class Days(models.Model):
        day = models.CharField(max_length=8)

        def __str__(self):
            return self.day

    shw_days = models.ManyToManyField(Days)

    def __str__(self):
        return self.shw_title + ' with - ' + self.shw_hosts


class Episode(models.Model):
    ep_show = models.ForeignKey(Show, on_delete=models.CASCADE)
    ep_title = models.CharField(max_length=250)
    ep_file_type = models.CharField(max_length=10)
    ep_release_date = models.DateField(blank=True, null=True, verbose_name="Release Date")

    def __str__(self):
        return self.ep_title
