from django.db import models

class Account(models.Model):
    username = models.EmailField(max_length = 140, unique= True)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return u'%s %s' % (self.username, self.password)