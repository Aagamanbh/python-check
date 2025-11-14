#password strength checker
print("Welcome to password strength checker.")
password=input("Enter you password: ")
if len(password)<6:
    Strength="Weak"
elif len(password)<=10:
    Strength="Medium"
else:
    Strength="Hard"
print(f"Password strength= {Strength}")
if password.islower():
    print("Error:Include Capital letter also.")
    