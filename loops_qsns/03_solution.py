# Multiplication table and skip fifth iteration
number=int(input("Enter the number:"))
for n in range(1,11):
   
    print(f"The multiplication table of {number}: \n")
for  i in range(1,11):
    if i==5:
        continue
    multiply= number*i
   
    print(f"{number}X{i}= {multiply}")