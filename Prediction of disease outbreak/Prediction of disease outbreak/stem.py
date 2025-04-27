import streamlit as st
import pandas as pd
import time

# Page setup
st.set_page_config(page_title="Patient Health Monitor", page_icon="🩺", layout="wide")
st.title("🩺 Real-Time Patient Monitoring Dashboard")

# File path
excel_file = 'C:/Users/saura/Desktop/Prediction of disease outbreak/patient_data.xlsx'

# Refresh every 5 seconds
refresh_interval = 5  # seconds

# Add an auto-refresh using Streamlit's `st.experimental_data_editor` trick
placeholder = st.empty()

while True:
    with placeholder.container():
        try:
            df = pd.read_excel(excel_file)

            if not df.empty:
                st.subheader("📈 Latest Readings")
                st.dataframe(df.tail(10))

                # Make sure 'Timestamp' column is datetime if needed
                if not pd.api.types.is_datetime64_any_dtype(df['Timestamp']):
                    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

                st.line_chart(df.set_index('Timestamp')[['BPM', 'Temperature']])

            else:
                st.warning("No data yet. Waiting for readings...")

        except Exception as e:
            st.error(f"Failed to load data: {e}")

        time.sleep(refresh_interval)
        st.rerun()  # << Use st.rerun() instead of experimental_rerun()
