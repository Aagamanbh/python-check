def inches_to_cm(inches):
    return inches*2.54

n=int(input("Enter the value in inch:"))
cm=inches_to_cm(n)
print(f"The value of {n}inch is {cm}cm ")