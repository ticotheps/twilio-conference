from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from decouple import config
from twilio.twiml.voice_response import Dial, VoiceResponse

CONF_PIN = config("CONF_PIN", cast=int)
MAX_PARTICIPANTS = config("MAX_PARTICIPANTS", default=2, cast=int)
NUM_DIGITS = config("NUM_DIGITS", default=4, cast=int)

@csrf_exempt
def my_conference_line(self):
    response = VoiceResponse()
    
    if 'Digits' in request.POST:
        conf_pin = request.POST['Digits']
    
        if conf_pin == CONF_PIN:  # <- set desired PIN in .env
            response.say("Welcome to the TireTutor Conference Room!")
            dial = Dial()
            dial.conference('TireTutor Conference Room',
                max_participants=MAX_PARTICIPANTS,
            )
            response.append(dial)
        
            return HttpResponse(str(response))
        else:
            response.say("Wrong PIN")
    
    else:
        gather = Gather(num_digits=NUM_DIGITS)
        gather.say("Please enter the conference PIN number.")
        response.append(gather)

    return HttpResponse(str(response))