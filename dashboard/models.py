from django.db import models

class Slot(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.BooleanField(default=False)
    user = models.EmailField(max_length = 140, blank=True, null= True)

    def __str__(self):
        return u'%s %s %s %s' % (self.start_time, self.end_time, self.status, self.user)