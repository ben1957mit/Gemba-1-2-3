import streamlit as st
from utils.auth import login, logout

st.title("Gemba Walk App")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login(username, password):
            st.success("Logged in successfully!")
            st.rerun()
        else:
            st.error("Invalid username or password")
else:
    st.write("Welcome to the Gemba Walk App!")
# ---------------------------
# Instructions Section (Home)
# ---------------------------

st.title("Gemba Walk App Instructions")

st.markdown("""
### 🧭 What This App Does
This app guides supervisors and team leads through **Daily** and **Weekly Gemba Walks** using simple, structured forms.  
It helps you:
- Record shift details  
- Capture observations and issues  
- Score performance  
- Track corrective actions  
- Produce clean summaries for follow‑up  

---

### 🔐 How to Log In
1. Open the app link.  
2. On the **Home** page, enter your username and password.  
3. Click **Login**.  
4. Once logged in, the sidebar unlocks the Daily and Weekly pages.

If you see “Please log in,” return to **Home** in the sidebar.

---

### 📂 Navigating the App
Use the **left sidebar** to move between pages:

- **Home** – Login and instructions  
- **Daily Gemba Walk** – Record daily observations  
- **Weekly Gemba Walk** – Summarize weekly performance  
- **Notes** – Optional space for reminders or comments  

---

### 📅 Daily Gemba Walk – How to Use It
Use this page during your daily walk-through.

#### 1. Enter Date & Shift Information
- Select the **Gemba Walk Date**  
- Enter **Shift Start** and **Shift End** times  

#### 2. Enter Walk Timing
- Enter **Walk Start** and **Walk End** times  

#### 3. Enter Personnel
- Supervisor Name  
- Team Lead Name  

#### 4. Select the Area Observed
Choose the area you reviewed (Receiving, Picking, Packing, Shipping, etc.).

#### 5. Record Issues & Observations
- Describe the issue or observation  
- Select **Severity Level** (Low → Critical)  
- Enter **Corrective Action Taken**  
- Assign a **Responsible Person**  
- Set a **Follow‑up Due Date**  

#### 6. Save the Daily Walk
Click **Save Daily Gemba Walk** to generate a summary.

---

### 📊 Weekly Gemba Walk – How to Use It
Use this page at the end of each week.

#### 1. Select the Week
- Choose the **Week Start Date**  
- The app calculates the **Week End Date**  

#### 2. Enter Personnel
- Supervisor Name  
- Team Lead Name  

#### 3. Enter Daily Findings
For each day (Monday–Friday), enter:
- Observations  
- Issues  
- Notes  

#### 4. Score the Week
Use the slider to rate the week from **0 (Poor)** to **10 (Excellent)**.

#### 5. Identify Top Issues
List the most important issues discovered during the week.

#### 6. Record Corrective Actions
Describe actions taken or planned.

#### 7. Save the Weekly Walk
Click **Save Weekly Gemba Walk** to generate a full summary.

---

### 💡 Tips for Best Use
- Complete the Daily Walk during or right after your walk-through.  
- Complete the Weekly Walk every Friday or at week’s end.  
- Use consistent names for supervisors and team leads.  
- Use the severity scale honestly to highlight real issues.  
- Assign follow-up actions clearly so nothing gets missed.  

---
""")
