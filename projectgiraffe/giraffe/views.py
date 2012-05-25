from django.shortcuts import render_to_response, Http404
from django.template import RequestContext
from django.utils import timezone

from giraffe.models import Giraffeword, GiraffewordForm

from hashlib import sha1
import datetime

def index(request):
    form = GiraffewordForm()

    return render_to_response('index.html',
        {'form': form},
        context_instance=RequestContext(request))

def newpassword_view(request):
    newpass = request.POST['password']

    # add this new password to the database, and stuff
    g = Giraffeword()
    # Some encryption should probably go on here
    g.password = newpass
    g.added_date = timezone.now()
    g.url = sha1(newpass + str(g.added_date)).hexdigest()
    g.save()

    return render_to_response('newpassword.html',
                              {'giraffe': g })


def pass_view(request, pass_hash):
    g = Giraffeword.objects.get(url=pass_hash)
    
    if g.password == None:
        return render_to_response('expired.html')


    # check to see if it has expired
    

    # Only ever allow one view, delete the password now
    password = g.password
    g.password = None
    g.save()

    return render_to_response('displaypass.html',
                              {'password': password })
