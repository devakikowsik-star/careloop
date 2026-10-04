def get_events(scenario):
    # scenario is a word we pass in: "normal" or "no_activity"

    if scenario == "normal":
        return [
            {"time": "07:30", "type": "doorbell", "note": "milk delivery"},
            {"time": "11:00", "type": "motion", "note": "neighbour visit"},
            {"time": "16:10", "type": "doorbell", "note": "courier"},
            {"time": "19:00", "type": "motion", "note": "movement near door"},
        ]

    if scenario == "no_activity":
        return [
            {"time": "07:30", "type": "doorbell", "note": "milk delivery"},
        ]

    return []