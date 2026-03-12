import streamlit as st
from utils.auth import require_login
from utils.branding import add_branding, PRIMARY_YELLOW

require_login()
add_branding()

st.title("📆 Weekly Gemba Walk Schedule")

st.subheader("Purpose")
st.write("Review broader operational performance, validate corrective actions, and identify systemic improvement opportunities.")

st.subheader("Weekly Time Block")
st.write("**Day:** Wednesday")
st.write("**Time:** 2:00 PM")
st.write("**Duration:** 45–60 minutes")
st.write("**Participants:** Warehouse Manager, CI Lead, Safety Officer")

st.subheader("Weekly Focus Themes")
st.markdown(
    """
- **Week 1:** Safety & Compliance  
- **Week 2:** Inventory Accuracy & Control  
- **Week 3:** Equipment & Maintenance  
- **Week 4:** Process Flow & Layout Optimization  
"""
)

st.subheader("Weekly Review Items")
st.markdown(
    f"<div style='background:{PRIMARY_YELLOW}20; padding:8px; border-radius:4px;'>"
    "Use this list to guide your weekly review discussion.</div>",
    unsafe_allow_html=True,
)

review_items = [
    "KPI trends (accuracy, cycle time, dock-to-stock)",
    "Status of open corrective actions",
    "6S audit results",
    "Employee feedback themes",
    "Waste identification summary",
]

for item in review_items:
    st.checkbox(item)
