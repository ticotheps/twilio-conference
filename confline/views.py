from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from twilio.twiml.voice_response import Conference, Dial, VoiceResponse, Say

@csrf_exempt
def my_conference_line(request):
    response = VoiceResponse()
    
    target_number = config('TARGET_NUMBER')
    
    response.say(
        'Thank you for allowing TireTutor to make tire buying easier ' +
        'for you! Please wait while we connect you to your tire dealer now!')
    response.dial(target_number)
    
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