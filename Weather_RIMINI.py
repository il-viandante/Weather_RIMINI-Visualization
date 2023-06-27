import pandas as pd
from datetime import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

data = pd.read_csv("Weather_RIMINI.csv")
data = data.dropna()
#print(data)

# Get user input for the date range
start_date = pd.to_datetime(input("Enter start date (YYYY-MM-DD): "))
end_date = pd.to_datetime(input("Enter end date (YYYY-MM-DD): "))

# Convert the 'DATE' column to timestamp format
data['DATE'] = pd.to_datetime(data['DATE'])


# Filter the data based on the chosen date range
filtered_data = data[(data['DATE'] >= start_date) & (data['DATE'] <= end_date)]

plt.style.use('classic')

# Create the visualization
fig, ax = plt.subplots()

# Plotting lines for each parameter
ax.plot(data['DATE'], data['TAVG'], color='green')
ax.plot(data['DATE'], data['TMAX'], color='green')
ax.plot(data['DATE'], data['TMIN'], color='Red')
ax.plot(data['DATE'], data['PRCP'], color='purple')
ax.plot(data['DATE'], data['SNWD'], color='brown')


ax.text(data['DATE'].iloc[-1], data['TAVG'].iloc[-1], '  Avg_Temp F', color='orange')
ax.text(data['DATE'].iloc[-1], data['TMAX'].iloc[-1], '  Max_Temp F', color='Red')
ax.text(data['DATE'].iloc[-1], data['TMIN'].iloc[-1],'  Min_Temp F', color='green')
ax.text(data['DATE'].iloc[-1], data['PRCP'].iloc[-1], '  Precip', color='purple')
ax.text(data['DATE'].iloc[-1], data['SNWD'].iloc[-1], '  Snw_Dept', color='brown')


ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.xlabel('Date', fontsize=25, color='magenta')
plt.ylabel('Weather', fontsize=40, color='magenta')

# Format start_date and end_date as strings
start_date_str = start_date.strftime('%Y-%m-%d')
end_date_str = end_date.strftime('%Y-%m-%d')
ax.set_title('Weather Trends in Rimini  (' + start_date_str + ' to ' + end_date_str + ')')

#plt.title(title, fontsize=20)
ax.set_ylabel("Weather", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.legend()
plt.tight_layout()
plt.show()




