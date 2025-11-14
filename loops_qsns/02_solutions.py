#Calculation of sum of even number upto n number
even_number=int(input("Enter the number:"))
even_number_sum=0
for num in range(0,even_number+1):
    if num%2==0:
        even_number_sum+=1
print(f"The sum of even number is: {even_number_sum}")
    

