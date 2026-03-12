import streamlit as st

PRIMARY_RED = "#E74C3C"
PRIMARY_GREEN = "#2ECC71"
PRIMARY_YELLOW = "#F1C40F"

def add_branding():
    with st.sidebar:
        try:
            st.image("assets/logo.png", width=180)
        except Exception:
            st.markdown("### Gemba Walk App")

        st.markdown(
            f"""
            <div style='margin-top:10px;'>
                <div style='height:6px; background:{PRIMARY_GREEN};'></div>
                <div style='height:6px; background:{PRIMARY_YELLOW};'></div>
                <div style='height:6px; background:{PRIMARY_RED};'></div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("#### Warehouse Gemba System")
        st.markdown("---")

def status_tag(text, color):
    return (
        f"<span style='background:{color}; padding:4px 8px; "
        f"border-radius:4px; color:white; font-size:0.85rem;'>{text}</span>"
    )
