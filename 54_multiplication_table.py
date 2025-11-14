def mul(n,i):
    return n*i

n=int(input("Enter a number:"))
for n in range(1,11):
   print(f"Multiplication table of {n}")  # This is the code to print a multiplication table from 1 to 10.
   print("--"*25)
   for i in range(1,11):
    print(f"{n} X {i}={(mul(n,i))}")

   
# #    OR,
# def multiply(n,i):
#  return n*i
# n=int(input("Enter a number:"))
#     for i in  range(1,11):
#       print(f"{n}X{i}={n*i}")