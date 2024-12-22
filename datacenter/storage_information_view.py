from datacenter.models import Passcard, Visit
from datacenter.visit_duration import format_duration, get_duration, is_visits_long
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = [
        {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_duration(get_duration(visit)),
            'is_strange': is_visits_long(visit, minutes=60)
        }
        for visit in Visit.objects.filter(leaved_at=None)
    ]

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
