from django.http import HttpResponse
from .models import Reason
import requests, os
from LoveDb.settings import SECRET_KEY, IFTTT_KEY

def index(request):
    their_key = request.GET.get('key', '')
    my_key = SECRET_KEY

    if(their_key == my_key):
        reasons = Reason.objects.filter(been_used=False).order_by('-created_date')[:1]

        if(len(reasons) > 0):
            reason = reasons[0]
            
            love_note = {}
            love_note['value1'] = reason.reason_text

            # Send via If This Then That
            requests.post("https://maker.ifttt.com/trigger/send_love_note/with/key/{0}".format(IFTTT_KEY), data=love_note)

            # Update reason so that we don't use the same one twice (wouldn't that be embarrassing!)
            reason.been_used = True
            reason.save()


    return HttpResponse('<a href="http://crowdersoup.com">Made with Love, by CrowderSoup</a>')
