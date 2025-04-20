#Program for creating a Dictionary.

person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "profession": "Engineer"
}

print("Created Dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")