from django.db import models
from django import forms


class PhotoStatistic(models.Model):
    statistic = models.CharField(max_length=500)
    pub_time = models.DateTimeField(auto_now_add=True)


class Photo(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return "%s : %d 分" % (self.name, self.score)

    def __le__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    def serialize(self):
        return dict(id=self.id, name=self.name, score=self.score, filename=self.file_name)
