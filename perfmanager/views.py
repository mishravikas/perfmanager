from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from perfmanager.models import Alerts
import datetime
import json
import utils

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
    print request.POST['id'].split(',')
    alerts = Alerts.objects.filter(id__in=request.POST['id'].split(','))
    if typeval == 'status':
        print "changing status of alertids %s to %s" %(request.POST['id'],request.POST['status'])
        for alert in alerts:
            alert.status = request.POST['status']
            alert.save(update_fields=['status'])

    elif typeval == 'revision':
        print "changing Revision of alertids %s to %s" %(request.POST['id'],request.POST['revision'])

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
        print alerts
        for alert in alerts:
            print alert.id
            alert.email = request.POST['email']
            alert.comment = comment
            alert.save(update_fields=['email', 'comment'])
        print "DONE-----------------------------"

    elif typeval == 'branch':
        print "Adding branch to alertids %s to revision %s and branch %s" %(request.POST['id'],request.POST['revision'],request.POST['branch'])
    
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