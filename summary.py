def make_summary(events, result):
    count = len(events)

    if result == "alert":
        return f"Only {count} event(s) today and a very long quiet period. Please check on your parent."

    return f"{count} events today. Normal day."