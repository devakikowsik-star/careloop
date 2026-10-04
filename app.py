import streamlit as st
from ring_source import get_events
from rules import check_day
from summary import make_summary

st.title("CareLoop")
st.write("A daily check for a parent living alone.")

scenario = st.radio("Choose a day to view", ["normal", "no_activity"])

events = get_events(scenario)
result = check_day(events)
message = make_summary(events, result)

if result == "alert":
    st.error(message)
else:
    st.success(message)

st.subheader("Timeline")
st.table(events)

st.caption("Prototype with simulated data. Not an emergency service.")