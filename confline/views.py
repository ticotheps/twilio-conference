from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from twilio.twiml.voice_response import VoiceResponse, Say, Dial, Number

CALL_WHISPER_URL = config('CALL_WHISPER_URL')

@csrf_exempt
def my_conference_line(request):
    response = VoiceResponse()
    dial = Dial()
    
    target_number = config('TARGET_NUMBER')
    number = Number(target_number)
    
    response.say(
        'Thank you for allowing TireTutor to make tire buying easier ' +
        'for you! Please wait while we connect you to your tire dealer now!')
    dial.number(target_number, url=CALL_WHISPER_URL, method='GET')
    response.append(dial)
    
    return HttpResponse(str(response))