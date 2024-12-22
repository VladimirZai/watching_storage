from django.utils.timezone import localtime


SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = 60 * SECONDS_IN_A_MINUTE


def get_duration(visit):
    time_now = localtime()
    if not visit.leaved_at:
        return time_now - visit.entered_at
    return visit.leaved_at - visit.entered_at


def is_visits_long(visit, minutes=60):
    return get_duration(visit).total_seconds() > minutes * SECONDS_IN_A_MINUTE


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, SECONDS_IN_AN_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_IN_A_MINUTE)
    return f'{hours:02}:{minutes:02}:{seconds:02}'
