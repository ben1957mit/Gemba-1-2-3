import streamlit as st
from datetime import date, timedelta
from utils.auth import require_login

require_login()

st.title("Weekly Gemba Walk")

# --- Week Selection ---
week_start = st.date_input("Week Start Date", value=date.today())
week_end = week_start + timedelta(days=6)
st.write("**Week Range:**", week_start, "to", week_end)

# --- Personnel ---
st.subheader("Personnel")
supervisor = st.text_input("Supervisor Name")
team_lead = st.text_input("Team Lead Name")

# --- Daily Findings ---
st.subheader("Daily Findings")

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
daily_notes = {}

for day in days:
    daily_notes[day] = st.text_area(f"{day} Findings")

# --- Weekly Scoring ---
st.subheader("Weekly Performance Score")

score = st.slider(
    "Overall Weekly Score (0 = Poor, 10 = Excellent)",
    min_value=0,
    max_value=10,
    value=7
)

# --- Top Issues ---
st.subheader("Top Issues Identified This Week")
top_issues = st.text_area("List the top issues identified this week")

# --- Corrective Actions ---
st.subheader("Corrective Actions")
corrective_actions = st.text_area("Corrective Actions Taken or Planned")

# --- Completion Button ---
submitted = st.button("Save Weekly Gemba Walk")

# --- Summary ---
if submitted:
    st.success("Weekly Gemba Walk Saved")
    st.markdown("---")
    st.subheader("Weekly Summary")

    st.write("**Supervisor:**", supervisor)
    st.write("**Team Lead:**", team_lead)
    st.write("**Week:**", week_start, "to", week_end)
    st.write("**Weekly Score:**", score)
    st.write("**Top Issues:**", top_issues)
    st.write("**Corrective Actions:**", corrective_actions)

    st.subheader("Daily Notes")
    for day in days:
        st.write(f"**{day}:** {daily_notes[day]}")
