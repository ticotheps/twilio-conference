from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from twilio.twiml.voice_response import Conference, Dial, VoiceResponse, Say

CONF_PIN = config("CONF_PIN")
MAX_PARTICIPANTS = config("MAX_PARTICIPANTS", default=2, cast=int)
NUM_DIGITS = config("NUM_DIGITS", default=4, cast=int)

@csrf_exempt
def my_conference_line(request):
    response = VoiceResponse()
    dial = Dial()
    response.say("Thank you for allowing TireTutor to make tire buying easier for you! Please wait while we connect you to your tire dealer now.")
    dial.conference('TireTutor Conference Room', wait_url='http://demo.twilio.com/docs/classic.mp3')
    response.append(dial)

    return HttpResponse(str(response))