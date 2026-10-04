from ring_source import get_events
from rules import check_day

for scenario in ["normal", "no_activity"]:
    events = get_events(scenario)
    print("Scenario:", scenario)

    for e in events:
        print("  ", e["time"], e["type"], e["note"])

    print("Result:", check_day(events))
    print()