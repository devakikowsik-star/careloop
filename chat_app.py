import re
import streamlit as st
import tools

st.title("CareLoop")
st.caption("Simulated Alexa+ experience. Uses simulated home events, not a real device.")

scenario = st.sidebar.radio("Simulated day", ["normal", "no_activity"])

st.sidebar.markdown("**Try asking:**")
st.sidebar.write("- Is my mother okay today?")
st.sidebar.write("- Who visited today?")
st.sidebar.write("- When was the last activity?")
st.sidebar.write("- Give me an update")


def has_any(question, keywords):
    # True if any word in the question starts with one of the keywords
    words = re.findall(r"[a-z]+", question.lower())
    for word in words:
        for key in keywords:
            if word.startswith(key):
                return True
    return False


def answer(question):
    if has_any(question, ["visit", "doorbell", "guest", "came", "knock", "deliver", "courier"]):
        return tools.last_visitor(scenario)

    if has_any(question, ["ok", "fine", "safe", "alright", "well", "worr", "health", "good"]):
        return tools.is_everything_ok(scenario)

    if has_any(question, ["last", "when", "activity", "recent", "latest", "move", "motion"]):
        return tools.last_activity_time(scenario)

    return tools.today_summary(scenario)


if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(m["content"])

question = st.chat_input("Ask something, for example: Is my mother okay today?")
if question:
    st.session_state.messages.append({"role": "user", "content": question})
    st.session_state.messages.append({"role": "assistant", "content": answer(question)})
    st.rerun()