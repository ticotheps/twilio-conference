from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.voice_response import Dial, VoiceResponse

@csrf_exempt
def my_conference_line(self):
    response = VoiceResponse()
    dial = Dial()
    
    dial.conference('TireTutor Conference Room')
    response.append(dial)
    
    return HttpResponse(str(response))
