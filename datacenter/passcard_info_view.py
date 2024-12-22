from datacenter.models import Passcard, Visit
from datacenter.visit_duration import format_duration, get_duration, is_visits_long
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard_visits = [
        {
            'entered': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visits_long(visit, minutes=60)
        }
        for visit in Visit.objects.filter(passcard__passcode=passcode)
    ]

    context = {
        'passcard': get_object_or_404(Passcard, passcode=passcode),
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
