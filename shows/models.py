from django.db import models


class Station(models.Model):
    st_name = models.CharField(max_length=250)
    st_icon = models.CharField(max_length=1000)
    st_freq = models.CharField(max_length=100)


class Show(models.Model):
    shw_title = models.CharField(max_length=250)
    shw_hosts = models.CharField(max_length=250)
    shw_icon = models.CharField(max_length=1000)
    shw_station = models.ForeignKey(Station, on_delete=models.CASCADE)
    shw_live_on_time = models.TimeField
    shw_live_off_time = models.TimeField


class Episode(models.Model):
    ep_show = models.ForeignKey(Show, on_delete=models.CASCADE)
    ep_title = models.CharField(max_length=250)
    ep_file_type = models.CharField(max_length=10)
    ep_release_date = models.DateField
