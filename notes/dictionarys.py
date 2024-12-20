customer = {
    "name": "John Doe",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(f"{customer['age']}")
print(customer.get("birthdate")) #replys with none as its not there
#can update by:
customer["name"] = "Titas"