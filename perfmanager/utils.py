from perfmanager.models import Alerts
from django.db.models import Q
import datetime
from mozci.sources.buildapi import query_repo_url
from mozci.sources.pushlog import query_revisions_range_from_revision_and_delta
from django.conf import settings

def get_merged_alerts():
    retVal = {}
    delta = datetime.datetime.today()-datetime.timedelta(days=126)
    query=(Q(status='')|Q(status='NEW')|Q(status='Investigating'))&Q(push_date__gt=delta)
    merged_alerts = Alerts.objects.filter(query).exclude(mergedfrom__isnull=True).exclude(mergedfrom__exact='')
    # print merged_alerts.query
    for alert in merged_alerts:
        # print alert.id
        row = {'backout': alert.backout, 'branch': alert.branch, 'bug':alert.bug, 'bugcount':alert.bugcount, 'changeset': alert.changeset, 'comment': alert.comment, 'duplicate': alert.duplicate,
                'email': alert.email, 'graphurl': alert.graphurl, 'id': alert.id, 'keyrevision': alert.keyrevision, 'mergedfrom': alert.mergedfrom, 'percent': alert.percent, 'platform': alert.platform,
                'push_date': alert.push_date.strftime("%Y-%m-%d %H:%M:%S"), 'status': alert.status, 'treeherderurl': alert.treeherderurl, 'test': alert.test}

        if alert.keyrevision in retVal:
            retVal[alert.keyrevision].append(row)
        else:
            retVal[alert.keyrevision] = [row]

    return retVal

def get_merged_alerts_by_keyrev(keyrev):
    retVal = {}
    merged_alerts = Alerts.objects.filter(keyrevision=keyrev).exclude(mergedfrom__isnull=True).exclude(mergedfrom__exact='')

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

def get_alerts_by_keyrev(keyrev):
    alerts = Alerts.objects.filter(keyrevision=keyrev)
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

def get_revision_range(repo_name, revision):
    """
    Query pushlog in mozci and return revisions in a range of six.
    """
    print repo_name, revision
    try:
        if repo_name == 'mobile':
            repo_name = 'mozilla-central'

        repo_url = query_repo_url(repo_name)
        print repo_url
        revlist = query_revisions_range_from_revision_and_delta(repo_url, revision, delta=6)
    except Exception,e:
        print e
        print "exception while getting repo: %s, revision: %s" % (repo_name, revision)
        raise

    return revlist[0], revlist[-1]

def build_tbpl_link(record):
    # TODO: is branch valid?
    tbpl_branch = record.branch.split('-Non-PGO')[0]
    if tbpl_branch == 'Firefox':
        treeherder_repo = 'mozilla-central'
    else:
        treeherder_repo = tbpl_branch.lower()

    vals = get_revision_range(treeherder_repo, record.keyrevision)

    link = ''
    if vals:
        params = []

        tbpl_platform = settings.TBPL_PLATFORMS[record.platform]
        tbpl_test = settings.TBPL_TESTS[record.test]['jobname']
        tbpl_tree = settings.TBPL_TREES[record.branch]

        if 'OSX' in tbpl_platform:
            tbpl_tree = tbpl_tree.split(' pgo')[0]

        params.append(('repo', treeherder_repo))
        params.append(('fromchange', vals[0]))
        params.append(('tochange', vals[1]))
        params.append(('filter-searchStr', '%s %s talos %s' % (tbpl_platform, tbpl_tree, tbpl_test)))
        link = settings.TREEHERDER_URL
        delim = '?'
        for key, value in params:
            link = "%s%s%s=%s" % (link, delim, key, value)
            if delim == '?':
                delim = '&'
        link = link.replace(' ', '%20')

    return link
