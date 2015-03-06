from django.db import models

class Alerts(models.Model):
    branch = models.CharField(max_length=128, null=False, default='')
    test = models.CharField(max_length=128, null=False, default='')
    platform = models.CharField(max_length=64, null=False, default='')
    percent = models.CharField(max_length=32, null=False, default='')
    graphurl = models.CharField(max_length=128, null=True, default='')
    changeset = models.CharField(max_length=128, null=False, default='')
    keyrevision = models.CharField(max_length=128, null=False, default='')
    bugcount = models.IntegerField(max_length=11, null=False, default=0)
    comment = models.CharField(max_length=1024, null=False, default='')
    bug = models.CharField(max_length=128, null=False, default='')
    status = models.CharField(max_length=64, null=False, default='')
    email = models.CharField(max_length=128, null=False, default='')
    push_date = models.DateTimeField(null=True)
    changesets = models.CharField(max_length=8192, null=False, default='')
    mergedfrom = models.CharField(max_length=128, null=False, default='')
    duplicate = models.CharField(max_length=128, null=True)
    treeherderurl = models.CharField(max_length=256, null=True)
    backout = models.CharField(max_length=128, null=True)

    def __unicode__(self):
        return u'alert id:%s keyrevision:%s' % (self.id, self.keyrevision)
