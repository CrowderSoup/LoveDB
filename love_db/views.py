from django.http import HttpResponse
from .models import Reason
import requests, os
from LoveDb.settings import SECRET_KEY, IFTTT_KEY

def index(request):
    their_key = request.GET.get('key', '')
    my_key = SECRET_KEY

    if(their_key == my_key):
        reason = Reason.objects.filter(been_used=False).order_by('-created_date')[:1]
        love_note = {}
        love_note['value1'] = reason[0].reason_text
        requests.post("https://maker.ifttt.com/trigger/send_love_note/with/key/{0}".format(IFTTT_KEY), data=love_note)

    return HttpResponse('<a href="http://crowdersoup.com">Made with Love, by CrowderSoup</a>')
