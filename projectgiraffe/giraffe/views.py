from django.shortcuts import render_to_response, Http404
from django.template import RequestContext
from django.utils import timezone

from giraffe.models import Giraffeword, IPLog
from giraffe.enc import encrypt, decrypt


from hashlib import sha1
import datetime

def index(request, error_message=None):

    return render_to_response('index.html',
        { 'error_message': error_message, },
        context_instance=RequestContext(request))

def newpassword_view(request):
    if not request.POST:
        raise Http404

    newpass = request.POST['password']
    duration = int(request.POST['duration'])
    secret = request.POST['secret'].lower()

    if len(newpass) == 0:
        return index(request, "You must enter a password!")

    if len(secret) == 0:
        return index(request, "You must enter a secret word!")


    if duration < 5 or duration > 60:
        return index(request, 
            "Invalid duration! Also, you are doing something fishy..")


    # add this new password to the database, and stuff
    g = Giraffeword()

    # encrypt using secret word
    # append a single | to aid in decrypting later
    g.password = encrypt(secret, newpass + "|")
    g.added_date = timezone.now()
    g.url = sha1(newpass + str(g.added_date)).hexdigest()
    g.duration = duration
    g.save()

    expire_time = timezone.now() + datetime.timedelta(minutes=g.duration)

    return render_to_response(
		'newpassword.html',
		{	'giraffe': g,
			'newpass': newpass,
			'secret' : secret,
			'expire' : expire_time, 
		},
		context_instance=RequestContext(request))


def pass_view(request, pass_hash):
    error_message = None


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

    # make sure the user has the secert word
    if not request.POST:

        return render_to_response('getpass.html',
            { 'error_message': error_message, 
              'giraffe': g, 
            
            },
            context_instance=RequestContext(request)
        )

    secret = request.POST['secret'].lower()

    # attempt to decrypt the password
    dpass = decrypt(secret, g.password)

    # Only ever allow one view, delete the password now
    g.password = None
    g.save()

    # if the password ends with a |, decryption worwked
    if dpass[-1:] != '|':
        log.expired = True
        log.save()
        return render_to_response('expired.html')

    else:
        dpass = dpass[:-1]  # cut off the last character


    log.save()
    return render_to_response('displaypass.html',
                              {'password': dpass })

