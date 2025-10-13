"""An example of how to represent a group of acquaintances in Python."""

# Your code to go here...
my_group = {
    "name": "vfdv52-Gumanji530",
    "members": [
        {"name": "Jill",
         "age": 26,
         "job": "biologist",
         "connections":{ 
         "friend": ["Zalika"],
         "partner": ["John"]}
         },
        {"name": "Zalika",
         "age": 28,
         "job": "Designer",
         "connections": {
         "friend": ["Jill"]}
         },
        {"name": "John",
         "age": 27,
         "job": "Writer",
         "connections": {
         "partner": ["Jill"]}
         },
        {"name": "Nash",
         "age": 34,
         "job": "Chef",
         "connections": {
         "cousin": ["John"],
         "landlord": ["Zalika"]}
        }
    ]
}

# Access example
print(f"Jill's age: {my_group['members'][0]['age']}")
print(f"Jill's friends: {my_group['members'][3]['connections']}")