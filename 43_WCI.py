def wind_chill_index(v, t):
    if (0<=v <=4):
        return f"wind chilled index is {t} F"
    elif v>=45:
        return f"wind chilled index is {1.6*t - 55} F"
    else:
        wci=91.4+ (91.4 - t)*(0.0203*v - 0.304*v*0.5-0.474)

v=float(input("Enter wind speed in miles per hour: "))
t=float(input("Enter air temperature in Fahrenheit: "))
print(wind_chill_index(v, t))
