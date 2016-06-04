from django.db import models
from django import forms


class PhotoStatistic(models.Model):
    statistic = models.CharField(max_length=500)
    pub_time = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return dict(pub_time=str(self.pub_time.strftime("%m-%d %H:%M:%S")), statistic=self.statistic)


class Photo(models.Model):
    NONE = 0
    WAITING = 1
    MATCHED = 2

    name = models.CharField(max_length=100, default="")
    score = models.CharField(max_length=20, default="")
    file_name = models.CharField(max_length=100, default="")

    match_status = models.SmallIntegerField(default=0)  # 0 - None 1 - Waiting for match 2 - matched
    match_key = models.CharField(max_length=10, default="")
    matched_id = models.CharField(max_length=100, default="")

    def __le__(self, other):
        return self.score < other.score

    def __eq__(self, other):
        return self.score == other.score

    def serialize(self):
        return dict(id=self.id, name=self.name, score=self.score, filename=self.file_name)

    def serialize_verbose(self):
        if self.match_status == self.NONE:
            m = "None"
        elif self.match_status == self.WAITING:
            m = "Waiting"
        elif self.match_status == self.MATCHED:
            m = "Matched"
        else:
            m = "Unknown"

        return dict(id=self.id, name=self.name, score=self.score, filename=self.file_name,
                    match_status=m, match_key=self.match_key, match_id=self.matched_id)
