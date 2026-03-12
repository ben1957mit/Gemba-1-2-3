import streamlit as st
from utils.auth import require_login
from utils.branding import add_branding

require_login()
add_branding()

st.title("🚶 Tailored Gemba Walk Path for Your Warehouse")

st.subheader("Recommended Route")
st.markdown(
    """
- **Receiving Dock:** Check unloading process, staging, and inspection  
- **Put-Away Zone:** Observe scanning accuracy and bin placement  
- **Bulk Storage & Racking:** Verify labeling, pallet condition, and organization  
- **Picking Areas:** Watch for travel paths, congestion, and accuracy checks  
- **Packing Stations:** Review ergonomics, materials availability, and quality checks  
- **Shipping Dock:** Confirm load verification and staging discipline  
- **Equipment Charging & Maintenance Area:** Inspect safety, cables, and equipment readiness  
"""
)

st.subheader("Key Observation Points")
st.markdown(
    """
- Actual workflow vs. documented SOPs  
- Employee workload balance  
- Waste (motion, waiting, rework, excess inventory)  
- Safety risks (forklift traffic, stacking, PPE)  
- Opportunities for visual management  
"""
)
