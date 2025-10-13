# def add_person(name, age, job, connections=None): 
#     """Function to create a new person dictionary.""" 
#     print("Adding a new person, if you don't want to add connections, just press enter.")
    
#     # Enter from terminal
#     name = input("Enter the person's name: ")
#     age = int(input("Enter the person's age: ")) # Convert to integer
#     job = input("Enter the person's job: ")
#     connections = input("Enter the person's connections (as a dictionary, e.g., {'friend': ['Alice']}): ")

#     if connections is None: 
#         connections = {} 
#     print(f"Added new person: {name}") 
#     return { 
#         "name": name, 
#         "age": age, 
#         "job": job, 
#         "connections": connections 
#     }

# Call function
# person = add_person(name, age, job)
# print(person)