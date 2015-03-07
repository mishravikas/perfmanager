from perfmanager.models import Alerts
from django.db.models import Q
import datetime


def get_merged_alerts():
    retVal = {}
    delta = datetime.datetime.today()-datetime.timedelta(days=126)
    query=(Q(status='')|Q(status='NEW')|Q(status='Investigating'))&Q(push_date__gt=delta)
    merged_alerts = Alerts.objects.filter(query).exclude(mergedfrom__isnull=True).exclude(mergedfrom__exact='')

    for alert in merged_alerts:
        row = {'backout': alert.backout, 'branch': alert.branch, 'bug':alert.bug, 'bugcount':alert.bugcount, 'changeset': alert.changeset, 'comment': alert.comment, 'duplicate': alert.duplicate,
                'email': alert.email, 'graphurl': alert.graphurl, 'id': alert.id, 'keyrevision': alert.keyrevision, 'mergedfrom': alert.mergedfrom, 'percent': alert.percent, 'platform': alert.platform,
                'push_date': alert.push_date.strftime("%Y-%m-%d %H:%M:%S"), 'status': alert.status, 'treeherderurl': alert.treeherderurl, 'test': alert.test}

        if alert.keyrevision in retVal:
            retVal[alert.keyrevision].append(row)
        else:
            retVal[alert.keyrevision] = [row]

    return retVal

def get_alerts():
    delta=datetime.datetime.today()-datetime.timedelta(days=126)
    query=Q(mergedfrom='')&(Q(status='')|Q(status='NEW')|Q(status='Investigating'))&Q(push_date__gt=delta)
    alerts = Alerts.objects.filter(query)
    retVal = {}
    for alert in alerts:
        row = {'backout': alert.backout, 'branch': alert.branch, 'bug':alert.bug, 'bugcount':alert.bugcount, 'changeset': alert.changeset, 'comment': alert.comment, 'duplicate': alert.duplicate,
                'email': alert.email, 'graphurl': alert.graphurl, 'id': alert.id, 'keyrevision': alert.keyrevision, 'mergedfrom': alert.mergedfrom, 'percent': alert.percent, 'platform': alert.platform,
                'push_date': alert.push_date.strftime("%Y-%m-%d %H:%M:%S"), 'status': alert.status, 'treeherderurl': alert.treeherderurl, 'test': alert.test}
        if alert.keyrevision in retVal:
            retVal[alert.keyrevision]['alerts'].append(row)
        else:
            retVal[alert.keyrevision] = {'alerts':[row]}

    return retVal