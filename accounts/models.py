from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True) 
    irc_nick = models.CharField(max_length=32, blank=True, null=True)
    receive_notifications = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s' % (self.user.email)