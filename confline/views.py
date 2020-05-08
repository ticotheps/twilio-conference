from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from twilio.twiml.voice_response import VoiceResponse, Say, Dial, Number

@csrf_exempt
def my_conference_line(request):
    response = VoiceResponse()
    dial = Dial()
    
    target_number = config('TARGET_NUMBER')
    number = Number(target_number)
    
    response.say(
        'Thank you for allowing TireTutor to make tire buying easier ' +
        'for you! Please wait while we connect you to your tire dealer now!')
    dial.number(target_number, url='http://demo.twilio.com/docs/classic.mp3')
    response.append(dial)
    
    return HttpResponse(str(response))

# @csrf_exempt
# def my_conference_line(request):
#     response = VoiceResponse()
#     dial = Dial()
#     response.say(
#         'Thank you for allowing TireTutor to make tire buying easier ' +
#         'for you! Please wait while we connect you to your tire dealer now.')
#     dial.conference(
#         'TireTutor Conference Room', 
#         beep=False,
#         wait_url='http://demo.twilio.com/docs/classic.mp3',
#         start_conference_on_enter=True,
#         end_conference_on_exit=True
#     )
#     response.append(dial)

#     return HttpResponse(str(response))

# On behalf of the whole TireTutor team, we would just like to say thank you for
# allowing us to make tire buying easier for you! Please wait while we connect
# you to your tire dealer now!