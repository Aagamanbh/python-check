"""
*
**
***
 """
# n=int(input("Enter a number:"))
# for i in range(0,n):
#     print("*"*(i+1),end="")
#     print("")

"""
***
* *   n=3
***

"""

n=int(input("Enter a number:"))
for i in range(1,n+1):
    if(i==1 or i==3):
     print("*"*(n),end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")