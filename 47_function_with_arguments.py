def greeting(ask,age,ending="Thankyou"):
    name=input("Enter a name:")
    print(f"Good morning,{name},{ask}")
    print(age)
    print(ending)
    return "done"

a=greeting("How are you?","How old are you?")
print(a)
