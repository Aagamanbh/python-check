def celcius_to_farenheit(celcius):
    return celcius*(9/5)+32

c=float(input("Enter the temperature:"))
f=celcius_to_farenheit(c)
print(f"{c}°C ia equals to {f}°F")