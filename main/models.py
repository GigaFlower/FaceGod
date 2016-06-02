from django.db import models
from django import forms


class PhotoStatistic(models.Model):
    statistic = models.CharField(max_length=500)
    pub_time = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return dict(pub_time=str(self.pub_time.strftime("%m-%d %H:%M:%S")), statistic=self.statistic)


class Photo(models.Model):
    name = models.CharField(max_length=100)
    score = models.CharField(max_length=20)
    file_name = models.CharField(max_length=100)

    def __le__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    def serialize(self):
        return dict(id=self.id, name=self.name, score=self.score, filename=self.file_name)
