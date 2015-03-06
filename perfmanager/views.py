from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from perfmanager.models import Alerts
from django.db.models import Q
import datetime
import json
from django.core import serializers

def index(request):
    delta=datetime.datetime.today()-datetime.timedelta(days=126)
    query=Q(mergedfrom='')&(Q(status='')|Q(status='NEW')|Q(status='Investigating'))&Q(push_date__gt=delta)
    alerts = Alerts.objects.filter(query)
    retVal = {}
    for alert in alerts:
        row = {'backout': alert.backout, 'branch': alert.branch, 'bug':alert.bug, 'bugcount':alert.bugcount, 'changeset': alert.changeset, 'comment': alert.comment, 'duplicate': alert.duplicate,
                'email': alert.email, 'graphurl': alert.graphurl, 'id': alert.id, 'keyrevision': alert.keyrevision, 'mergedfrom': alert.mergedfrom, 'percent': alert.percent, 'platform': alert.platform,
                'push_date': alert.push_date.strftime("%Y-%m-%d %H:%M:%S"), 'status': alert.status, 'treeherderurl': alert.treeherderurl, 'test': alert.test}
        if alert.keyrevision in retVal:
            retVal[alert.keyrevision].append(row)
        else:
            retVal[alert.keyrevision] = [row]
    return render(request, 'index.html',{'alerts':retVal})

def alertsbyrev(request):
    delta=datetime.datetime.today()-datetime.timedelta(days=126)
    query=Q(mergedfrom='')&(Q(status='')|Q(status='NEW')|Q(status='Investigating'))&Q(push_date__gt=delta)
    alerts = Alerts.objects.filter(query)
    retVal = {}
    for alert in alerts:
        row = {'backout': alert.backout, 'branch': alert.branch, 'bug':alert.bug, 'bugcount':alert.bugcount, 'changeset': alert.changeset, 'comment': alert.comment, 'duplicate': alert.duplicate,
                'email': alert.email, 'graphurl': alert.graphurl, 'id': alert.id, 'keyrevision': alert.keyrevision, 'mergedfrom': alert.mergedfrom, 'percent': alert.percent, 'platform': alert.platform,
                'push_date': alert.push_date.strftime("%Y-%m-%d %H:%M:%S"), 'status': alert.status, 'treeherderurl': alert.treeherderurl, 'test': alert.test}
        if alert.keyrevision in retVal:
            retVal[alert.keyrevision].append(row)
        else:
            retVal[alert.keyrevision] = [row]

    return HttpResponse(json.dumps(retVal), content_type="application/json")
