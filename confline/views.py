from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from twilio.twiml.voice_response import Dial, VoiceResponse, Gather

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
    
    # if 'Digits' in request.POST:
    #     conf_pin = request.POST['Digits']
    
    #     if conf_pin == CONF_PIN:  # <- set desired PIN in .env
    #         response.say("Thank you for allowing TireTutor to make tire buying easier for you! Please wait while we connect you to your tire experts.")
    #         dial = Dial()
    #         dial.conference(
    #             'TireTutor Conference Room',
    #             max_participants=MAX_PARTICIPANTS,
    #             wait_url='http://demo.twilio.com/docs/classic.mp3'
    #         )
    #         response.append(dial)
        
    #         return HttpResponse(str(response))
    #     else:
    #         response.say("Sorry, that PIN number is incorrect. Goodbye.")
    
    # else:
    #     gather = Gather(num_digits=NUM_DIGITS)
    #     gather.say("Please enter the conference PIN number.")
    #     response.append(gather)

    # return HttpResponse(str(response))