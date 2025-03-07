# streamlit_app.py
# Frontend made in streamlit which allows users to input the specific variables to generate a Business Plan.

import streamlit as st
import requests

# Streamlit app title
st.title("Business Plan Generator")

# Instructions
st.markdown("""
Enter the title of your Business, your business idea and the vision of your business
""")

# Input fields
var1 = st.text_input("Enter your Business Name:")
var2 = st.text_input("Enter your Business Idea:")
var3 = st.text_input("Enter the Vision of your Business:")

# Button to run the agents
if st.button("Run Business Plan Generator"):
    if var1 and var2 and var3:
        with st.spinner("Running agents..."):
            try:
                # Call the FastAPI backend
                response = requests.post(
                    "http://127.0.0.1:8000/run_agents",
                    json={"var1": var1, "var2": var2, "var3": var3}
                )
                if response.status_code == 200:
                    result = response.json()
                    st.success("Agents have completed the Business Plan Generation!")
                    st.text_area("Generator Output", result, height=300)
                else:
                    st.error(f"Error running agents: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Connection error: {e}")
    else:
        st.warning("Please enter all variables.")