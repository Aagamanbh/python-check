a="Make a lot of money"
b="buy now" 
c="subscribe this"
d="click this"    
word=input("Enter as you wanted: ")
if(a in word or b in word or c in word or d in word):   # form here we know the use of in 
    print("This comment is  spam.")
else:
    print("This comment is not spam.")

print("Thank-you") 