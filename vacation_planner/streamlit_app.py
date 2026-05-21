import streamlit as st
from vacation_planner.crew import VacationPlanner

st.title("✈️ AI Vacation Planner")
st.write("Let AI agents plan your perfect trip!")

destination = st.text_input("Where do you want to go?", placeholder="e.g. Tokyo, Japan")

if st.button("Plan My Vacation!"):
    if destination:
        with st.spinner("Your AI agents are planning your trip..."):
            inputs = {"topic": destination}
            result = VacationPlanner().crew().kickoff(inputs=inputs)
            st.success("Done!")
            st.markdown(result.raw)
    else:
        st.warning("Please enter a destination!")