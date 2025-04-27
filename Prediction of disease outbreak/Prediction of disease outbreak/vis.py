import pandas as pd
import matplotlib.pyplot as plt


file_path = 'C:/Users/saura/Desktop/Prediction of disease outbreak/patient_data.xlsx'  
df = pd.read_excel(file_path)


df['Timestamp'] = pd.to_datetime(df['Timestamp'])


df.set_index('Timestamp', inplace=True)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['BPM'], label='Heart Rate (BPM)', color='blue', marker='o')
plt.plot(df.index, df['Temperature'], label='Temperature (°F)', color='red', marker='x')

plt.title('Patient Health Monitoring')
plt.xlabel('Timestamp')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

# Printing values used for plotting
print("\n--- Plotted Data Points ---")
for timestamp, row in df.iterrows():
    print(f"Time: {timestamp} | BPM: {row['BPM']} | Temperature: {row['Temperature']:.1f} °F")
