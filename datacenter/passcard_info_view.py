from datacenter.models import Passcard, Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    passcard_visits = Visit.objects.filter(passcard=passcard)

    for visit in passcard_visits:
        this_passcard_visits = [
            {
                'entered_at': visit.entered_at,
                'duration': visit.format_duration(), 
                'is_strange': visit.is_visit_long(),
            },
        ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
