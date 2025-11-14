character=input("Enter a word  that contain repeated letters: ")
for i in character:
    if character.count(i)==1:
     print(i)
     break
else:
    print("It doesnt contain any single character.")
      
      
    

