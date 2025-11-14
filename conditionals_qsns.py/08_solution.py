marks={"Aagaman": 100,
       "Shovan": "K xa",
       "Shojan": [1,2,3,4]}
print(type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Aagaman":99,"Ashlesha":"Hello19"})
print(marks)
print(marks.get("Aagaman31")) #this will return none if the key is not is dictionary
print(marks["Aagaman31"]) #this will give an error.