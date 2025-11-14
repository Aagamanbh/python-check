#Grade Calculator
print("Welcome to Grade Calculator.")
user_marks=int(input("Enter your marks: "))
if user_marks>=90 and user_marks<=100:
    Grade="A"
elif user_marks>=80 and user_marks<=89:
    Grade="B"
elif user_marks>=70 and user_marks<=79:
    Grade="C" 
elif user_marks>=60 and user_marks<=69:
    Grade="D"
else:
    Grade="F"
print(f"Your grade is: {Grade}")
print("Thankyou!!")