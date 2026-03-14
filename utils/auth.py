import streamlit as st

def require_login():
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.warning("Please log in to continue.")
        st.stop()

def login(username, password):
    # Replace with your real credentials or database lookup
    if username == "admin" and password == "password":
        st.session_state["logged_in"] = True
        return True
    return False

def logout():
    st.session_state["logged_in"] = False
