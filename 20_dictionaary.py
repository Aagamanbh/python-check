sets={
    "Aagaman":200,   #here the left one is called keys ex:"Aagaman" & right ones are  called values. ex: :200
    "Radha":100,
    0:"Harry"
}

# print(sets["Aagaman"])
# print(sets,type(sets))
# print(sets.keys())
# print(sets.values())
# sets.update({"Ashlesha":300,"Anish":30})
# print(sets)

# print(sets.get("Aagaman")) #here it give none as output if the assigned name/Key is not found in the dictionaray.
# print(sets["Aagaman"]) #Here it gives error if the assigned value/Key is not found one the above dictionary
print(sets.items())
