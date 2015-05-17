from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    ageGroup = models.IntegerField()
    city = models.TextField()

    def __unicode__(self):
        return self.user.username + str(self.ageGroup) + self.city