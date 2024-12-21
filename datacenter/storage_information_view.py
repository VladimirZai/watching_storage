from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.visit_duration import format_duration, get_duration, is_visits_long
from django.shortcuts import render



def storage_information_view(request):
    non_closed_visits = []
    visits = Visit.objects.filter(leaved_at=None)

    for visit in visits:
        name = visit.passcard.owner_name
        entered = visit.entered_at
        duration = format_duration(get_duration(visit))
        is_strange = is_visits_long(visit, minutes=60)

        non_closed_visits.append({
            'who_entered': name,
            'entered_at': entered,
            'duration': duration,
            'is_strange': is_strange
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
