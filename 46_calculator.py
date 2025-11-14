print("Welcome to Aagaman's Calculator:")
num1=int(input("Enter a number:"))
operator=(input("Choose operator:'+','-','*','/':"))
num2=int(input("Enter a number:"))
if operator=='+':
    value=num1+num2
elif operator=='-':
    value=num1=num2
elif operator=='*':
    value=num1*num2
elif operator=='/':
    if(num2!=0):
        value=num1/num2
    else:
        value="num2 cant be zero."
else:
    value="invalid operator"


    
print(value)