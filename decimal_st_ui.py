import streamlit as st
from datetime import datetime

st.set_page_config(page_title="GBO's Decimal Year Converter", page_icon="📅", layout="centered")

st.markdown("""

<h1>📅 <a href="https://greatbasinobservatory.org/" style="text-decoration: none; color: #51A5B1;">GBO's</a> Decimal Year Convertor</h1>


            """, 
                unsafe_allow_html=True
)
st.write("Convert any date into its decimal year form (e.g. 2025.678).")

# --- Input ---
date_input = st.date_input("Select the date of your observation", value=datetime.today())

# --- Compute ---
year = date_input.year
start_of_year = datetime(year, 1, 1)
start_of_next_year = datetime(year + 1, 1, 1)
days_in_year = (start_of_next_year - start_of_year).days
days_passed = (datetime.combine(date_input, datetime.min.time()) - start_of_year).days
decimal_year = year + (days_passed / days_in_year)

# --- Output ---
st.markdown(f""" 

<div style="text-align: center;">
  <span style="font-size: 2em; font-weight: bold;">Decimal Year: </span>
  <h3>{decimal_year:.6f}</h3>
</div>


""", unsafe_allow_html=True)

st.divider()

#html in st 
st.markdown(
    """
    <div style="text-align: center; font-size: 1em; font-weight: bold;">
    <a href = "https://greatbasinobservatory.org/" style = 'text-decoration: none; color: #51A5B1;'>Learn More About Great Basin Observatory (GBO)</a>
      | Developed by <a href="https://www.linkedin.com/in/wijdan-ali-374793288/" style =' text-decoration: none; color: #51A5B1;'>Wijdan Ali</a>
    </div>
    """,
    unsafe_allow_html=True
)


