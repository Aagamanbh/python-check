# temperature conversion
unit=input("Enter the unit of temperature celcius or farenheit(C/F): ").lower()
temp=float(input("Enter temperature : "))
if unit=="c":
    result=(temp*9)/5+32
    unit="F"
    print(f"The temperature is {round(result,1)}°{unit}.")
elif unit=="f":
    result=(temp-32)*5/9
    unit="C"
    print(f"The temperature is {round(result,1)}°{unit}.")
else:
    print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
