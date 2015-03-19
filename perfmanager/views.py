from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render, get_list_or_404
from perfmanager.models import Alerts
import datetime
import json
import utils

class Record(object):
    def __init__(self, test, platform, branch, keyrevision):
        self.test = test
        self.platform = platform
        self.branch = branch
        self.keyrevision = keyrevision

def index(request):
    retVal = utils.get_alerts()
    merged_alerts = utils.get_merged_alerts()
    for key,value in merged_alerts.items():
        exists = retVal.get(key, None)
        if exists:
            retVal[key]['merged_alerts'] = value
        else:
            retVal[key] = {}
            retVal[key]['merged_alerts'] = value

    return render(request, 'index.html',{'alerts':retVal})

def alertsbyrev(request):
    retVal = utils.get_alerts()
    merged_alerts = utils.get_merged_alerts()
    for key,value in merged_alerts.items():
        exists = retVal.get(key, None)
        if exists:
            retVal[key]['merged_alerts'] = value
        else:
            retVal[key] = {}
            retVal[key]['merged_alerts'] = value

    return HttpResponse(json.dumps(retVal, indent=2), content_type="application/json")

def mergedalerts(request):
    retVal = utils.get_merged_alerts()

    return HttpResponse(json.dumps(retVal, indent=2), content_type="application/json")

@ensure_csrf_cookie
def updatefields(request):
    print "--------------STARTING TO UPDATE FIELDS----------------"
    typeval = request.GET.get('type','')

    alerts = Alerts.objects.filter(id__in=request.POST['id'].split(','))

    if typeval == 'status':
        print "changing status of alertids %s to %s" %(request.POST['id'],request.POST['status'])
        for alert in alerts:
            alert.status = request.POST['status']
            alert.save(update_fields=['status'])

    elif typeval == 'revision':
        print "changing Revision of alertids %s to %s" %(request.POST['id'],request.POST['revision'])
        for alert in alerts:
            record = Record(alert.test, alert.platform, alert.branch, alert.keyrevision)
            new_tbplurl = utils.build_tbpl_link(record)
            alert.keyrevision = request.POST['revision']
            alert.treeherderurl = new_tbplurl
            alert.save(update_fields=['keyrevision','treeherderurl'])

    elif typeval == 'bug':
        print "Adding bug to alertids %s bug no: %s" %(request.POST['id'],request.POST['BugID'])
        for alert in alerts:
            alert.bug = request.POST['BugID']
            alert.status = 'Investigating'
            alert.save(update_fields=['bug','status'])

    elif typeval == 'comment':
        comment = "[%s] %s" %(request.POST['email'], request.POST['comment'])
        print comment
        print "Adding comment to alertids %s with [%s] : %s" %(request.POST['id'],request.POST['email'],request.POST['comment'])
        for alert in alerts:
            print alert.id
            alert.email = request.POST['email']
            alert.comment = comment
            alert.save(update_fields=['email', 'comment'])

    elif typeval == 'branch':
        print "Adding branch to alertids %s to revision %s and branch %s" %(request.POST['id'],request.POST['revision'],request.POST['branch'])
        for alert in alerts:
            record = Record(alert.test, alert.platform, request.POST['branch'], request.POST['revision'])
            new_tbplurl = utils.build_tbpl_link(record)
            alert.branch = request.POST['branch']
            alert.keyrevision = request.POST['revision']
            alert.treeherderurl = new_tbplurl
            alert.save(update_fields=['branch','keyrevision','treeherderurl'])
    
    elif typeval == 'duplicate':
        print "Duplicate of alertids %s to %s" %(request.POST['id'],request.POST['rev'])
        for alert in alerts:
            alert.mergedfrom = request.POST['rev']
            alert.duplicate = request.POST['rev']
            alert.status = 'Duplicate'
            alert.save(update_fields=['mergedfrom','duplicate','status'])

    elif typeval == 'backout':
        print "Backout of alertids %s to %s" %(request.POST['id'],request.POST['bug'])
        for alert in alerts:
            alert.status = 'Backout'
            alert.bug = request.POST['bug']
            alert.save(update_fields=['status','bug'])


    return HttpResponse("DONE")

def revision(request, keyrev):
    alerts = get_list_or_404(Alerts, keyrevision=keyrev)
    retVal = utils.get_alerts_by_keyrev(keyrev)
    merged_alerts = utils.get_merged_alerts_by_keyrev(keyrev)
    for key,value in merged_alerts.items():
        exists = retVal.get(key, None)
        if exists:
            retVal[key]['merged_alerts'] = value
        else:
            retVal[key] = {}
            retVal[key]['merged_alerts'] = value
    return render(request, 'keyrev.html',{'alerts':retVal})