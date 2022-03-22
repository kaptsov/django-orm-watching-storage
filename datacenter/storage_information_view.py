
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)
    for visit in non_closed_visits:
      visit.who_entered = visit.passcard.owner_name
      visit.duration = visit.format_duration()
      visit.is_strange = visit.is_visit_long()
      
    context = {        
        'passcard': visit.passcard,
        'non_closed_visits': non_closed_visits, 
    }
    return render(request, 'storage_information.html', context)