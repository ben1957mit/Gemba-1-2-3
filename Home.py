import streamlit as st
from utils.auth import require_login
from utils.branding import add_branding

st.set_page_config(
    page_title="Gemba Walk App",
    page_icon="📦",
    layout="wide"
)

require_login()
add_branding()

st.title("📦 Warehouse Gemba Walk System")
st.write(
    "Use the page menu (top left) to navigate Daily, Weekly, KPI, and Action Tracking tools "
    "for your warehouse Gemba routines."
)

st.markdown("---")
st.subheader("How to Use This App")
st.markdown(
    """
- **Daily Gemba Walk**: daily route and checklist  
- **Weekly Gemba Walk**: broader performance review  
- **Warehouse Walk Path**: visual route guide  
- **Action Tracking**: log issues and employee feedback  
- **KPI Dashboard**: color-coded performance view  
- **Monthly Summary**: trends and improvements  
- **Notes**: general observations and ideas  
"""
)
