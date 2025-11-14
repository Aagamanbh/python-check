character_name ="aagaman"
character_age="40"
print("There was a person named "+ character_name + ",") #character_name is used to make program easier.using this we dont need to edit name or age searching the lines
print("He was "+ character_age + " years old")
character_name="King"
character_age="40"
print("He likes person named " + character_name+ ",")
print("He didnt like the age " + character_age+ ".")


phrase="Aagaman Industry"
print(phrase.upper().isupper()) # firstly converted into uppercase and then checked whether it is uppercase or not
print(len(phrase))   #to find out the length of the string
print(phrase[0])    # as string starts from zero so this line is used to provide the value stored in the location zero
print(phrase.index("I"))
print(phrase.replace("Aagaman" , "Bhattarai")) #replace tag is used to replace any string as per ouer choice
print(phrase.replace("Industry","Factory"))



my_num =5  #this is not a sting so we need to convert it into string before using any stings backside of a number
print(str(my_num)+ " is my favourite number") # Here we have converted number into sting so that it can be added in string.
my_num=-5
print(abs(my_num)) # this is to findd out the absolute value of the given number
print(pow(3,3)) # this is like 3^3
print(max(4,10)) # this is to find the larger number among two
print(min(0,10)) #this is to find the smaller number among two



from math import *
print(round(7.4))
print(sqrt(49))
print(floor(7.8))
print(ceil(2.8))




