favfruit = ["apple", "mango", "banana", "paloklok"]
fruit = "paloklok"
print("Favorite Fruits:")
for data in favfruit:
    print(data)
    if data == fruit:
        found = True
        print(f"{fruit} is one of my favorite fruits!")
        if not found:
    print(f"{fruit} is not one of my favorite fruits.")
    count = len(favfruit)
print(f"\nI have {count} favorite fruits.")