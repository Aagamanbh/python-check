#program to check if contains duplicate items in lists or not.

items=["apple","banana","apple","guava","Pineapple"]
unique_item=set()
for item in items:
    if item in unique_item:
        print(f"Duplicate item is: {item}")
    else:
        unique_item.add(item)

