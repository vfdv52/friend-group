name = ""
age = 0
job = ""
connections = {}

def forget_person(person1, person2):
    """Function to remove a connection between two people."""
    for relation, names in person1["connections"].items():
        if person2["name"] in names:
            names.remove(person2["name"])
            break
        else:
            print(f"{person1['name']} has no connection with {person2['name']}.")
        
    
def average_age(group):
    """Function to calculate the average age of the group members."""
    total_age = sum(member["age"] for member in group["members"])
    return total_age / len(group["members"])

def list_persons(group):
    """Function to list all persons in the group."""
    return [member["name"] for member in group["members"]]