from django.db import models

class schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    work = models.CharField(max_length=200)

    def __str__(self):
        return self.work
