# Program for deleting dictionary elements.

person = {
    "name": "ABC",
    "age": 18,
    "city": "Pune",
    "profession": "Engineer"
}

print("Before Deleting Dictionary Elements, Dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

delElement = dict.pop(person, "name")

print("After Deleting Dictionary Elements, Dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")