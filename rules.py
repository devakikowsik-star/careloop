DAY_START = "06:00"
DAY_END = "22:00"
MAX_GAP_HOURS = 12


def to_minutes(time_text):
    # Changes "07:30" into 450 (minutes since midnight)
    hours, minutes = time_text.split(":")
    return int(hours) * 60 + int(minutes)


def check_day(events):
    # If there are no events at all, it is an alert
    if len(events) == 0:
        return "alert"

    # Make a list of event times in minutes
    times = []
    for e in events:
        times.append(to_minutes(e["time"]))
    times.sort()

    # Add the start and end of the day to the list
    points = [to_minutes(DAY_START)] + times + [to_minutes(DAY_END)]

    # Find the biggest gap between two neighbouring points
    biggest_gap = 0
    for i in range(1, len(points)):
        gap = points[i] - points[i - 1]
        if gap > biggest_gap:
            biggest_gap = gap

    # If the biggest gap is 12 hours or more, it is an alert
    if biggest_gap >= MAX_GAP_HOURS * 60:
        return "alert"
    return "normal"