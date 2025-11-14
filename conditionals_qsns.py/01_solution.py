# movie tickets pricing
print("Welcome.Please select the movies and get the tickets.")
user_age=int(input("Enter your age: "))
day=input("Enter the day(s/m/t/w/t/f/sat): ").lower()
if user_age>=18:
    Ticket_price=12
else:
    Ticket_price=8
if day=="w":
    Ticket_price=Ticket_price-2
    print(f"The ticket price is:${Ticket_price}")
else:
    if user_age>=18:
        Ticket_price=12
    else:
        Ticket_price=8
print(f"The ticket_priceis:${Ticket_price}")

