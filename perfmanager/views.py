from django.http import HttpResponse, HttpResponseRedirect
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