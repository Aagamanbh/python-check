friends =["Aagaman","Kelvin","John","Aayush","Alok"]
lucky_number =[4,6,12,9,32]
print(friends[1:]) # here it gives the all value after kelvin including index 1
print(friends[1:4]) # here it gives the value between kelvin to aayush as it doesnt include last one
print(friends[0]) # here it gives the alue of index zero of friendds
print(friends[-1])  # here -1 means it gives the first value from end 
# friends.extend(lucky_number) # this extend function is used to add lucky numbers besides the friend
# friends.append("Mike") #here append means it adds the given string to the last
# friends.insert(1,"Aaship") # here insert function is used to insert value in index 1 and the vaue of index 1 will go onestep back

# friends.pop() #This pop function is used to remove the last element , it may be either string or any number
# friends.remove("John") #  remove is used to remove the given name

# friends.clear()

print(friends)
print(lucky_number)

