import serial
import pandas as pd
from datetime import datetime
import openpyxl


ser = serial.Serial('COM3', 115200, timeout=1)  


excel_file = 'C:/Users/saura/Desktop/Prediction of disease outbreak/patient_data.xlsx'

# Create Excel file if not exist
try:
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=['Timestamp', 'BPM', 'Temperature'])
    df.to_excel(excel_file, index=False)

while True:
    if ser.in_waiting:
        line = ser.readline().decode('utf-8').strip()
        
        if line.startswith("DATA"): 
            try:
                parts = line.split(',')
                bpm = int(parts[2])         
                temp = float(parts[3])      

                new_row = {
                    'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'BPM': bpm,
                    'Temperature': temp
                }

                df = pd.read_excel(excel_file)
                df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
                df.to_excel(excel_file, index=False)

                print(f"Saved: {new_row}")

            except Exception as e:
                print(f"Error parsing line: {line}, Error: {e}")
