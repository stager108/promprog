from django.db import models


class Task(models.Model):
    taskname = models.CharField(max_length=200)
    tasktext = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    is_imp = models.BooleanField()
    is_ready = models.BooleanField()
    def __str__(self):
        return self.taskname
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


