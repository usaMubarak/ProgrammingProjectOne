# Weather Severity Project

#initialize
total_rain = 0
total_wind = 0
days = 0

# Loop
while True:
    data = input()  # read rain and wind)
    values = data.split()  # split into two numbers
    rain = float(values[0])  # first number = rain
    if rain == -1.0:  # sentinel value to stop
        break
    wind = float(values[1])  # second number = wind
    total_rain += rain
    total_wind += wind
    days += 1

# calculate the average
avg_rain = total_rain / days
avg_wind = total_wind / days

# calculate the weather severity
severity = (avg_rain * 10) + avg_wind

# output results
print("The average rain is", round(avg_rain, 1), "inches")
print("The average wind is", round(avg_wind, 1), "mph")
print("The weather severity for these", days, "readings is:", round(severity, 1))
