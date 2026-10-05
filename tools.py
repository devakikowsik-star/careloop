from ring_source import get_events
from rules import check_day, to_minutes
from summary import make_summary


def today_summary(scenario="normal"):
    events = get_events(scenario)
    result = check_day(events)
    return make_summary(events, result)


def last_visitor(scenario="normal"):
    events = get_events(scenario)
    for e in reversed(events):
        if e["type"] == "doorbell":
            return f"The last doorbell was at {e['time']}: {e['note']}."
    return "No one has rung the doorbell today."


def is_everything_ok(scenario="normal"):
    events = get_events(scenario)
    if check_day(events) == "alert":
        return "No, there was a long quiet period. Please check on your parent."
    return "Yes, today looks normal."


def last_activity_time(scenario="normal"):
    events = get_events(scenario)
    if len(events) == 0:
        return "There has been no activity today."

    latest = events[0]
    for e in events:
        if to_minutes(e["time"]) > to_minutes(latest["time"]):
            latest = e
    return f"The last activity was at {latest['time']}: {latest['note']}."