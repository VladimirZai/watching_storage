from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.visit_duration import format_duration, get_duration, is_visits_long
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        entered = visit.entered_at
        duration = format_duration(get_duration(visit))
        is_strange = is_visits_long(visit, minutes=60)

        this_passcard_visits.append({
            'entered': entered,
            'duration': duration,
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
