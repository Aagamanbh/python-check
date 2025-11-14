# weight conversion 
name=input("Please enter your name: ")
weight=float(input("Enter your weight: "))
unit=input("Enter unit in kilogram or pound(K/L): ").lower()
if unit=="k":
    result=weight*2.205
    unit="lbs"
elif unit=="L":
    result=weight/2.205
    unit ="kg"
else:
    result="invalid unit.Enter in kilograms and pound only."
print(f"Hi {name}.\nYour weight is {result}{unit}.")