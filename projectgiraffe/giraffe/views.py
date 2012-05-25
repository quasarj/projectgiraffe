from django.shortcuts import render_to_response, Http404
from django.template import RequestContext
from django.utils import timezone

from giraffe.models import Giraffeword, IPLog

from hashlib import sha1
import datetime

def index(request):

    return render_to_response('index.html',
        context_instance=RequestContext(request))

def newpassword_view(request):
    newpass = request.POST['password']
    duration = int(request.POST['duration'])

    # add this new password to the database, and stuff
    g = Giraffeword()
    # Some encryption should probably go on here
    # use the 'secret word' as a key to encrypt with
    g.password = newpass
    g.added_date = timezone.now()
    g.url = sha1(newpass + str(g.added_date)).hexdigest()
    g.duration = duration
    g.save()

    return render_to_response('newpassword.html',
                              {'giraffe': g })


def pass_view(request, pass_hash):
    g = Giraffeword.objects.get(url=pass_hash)
    log = IPLog() 
    log.giraffeword = g
    log.ip = request.META['REMOTE_ADDR']
    log.added_date = timezone.now()

    # check to see if it has expired
    if g.password == None:
        log.expired = True
        log.save()
        return render_to_response('expired.html')

    # expired based on time
    if g.added_date < timezone.now() - datetime.timedelta(minutes=g.duration):
        # also delete the password from the db
        g.password = None
        g.save()
        log.expired = True
        log.save()
        return render_to_response('expired.html')

    # Only ever allow one view, delete the password now
    password = g.password
    g.password = None
    g.save()

    log.save()
    return render_to_response('displaypass.html',
                              {'password': password })
