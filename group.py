my_group = [
    {
        "name": "Jill",
        "age": 26,
        "job": "biologist",
        "connections": [
            {"relation": "friend", "person": "Zalika"},
            {"relation": "partner", "person": "John"}
        ]
    },
    {
        "name": "Zalika",
        "age": 28,
        "job": "artist",
        "connections": [
            {"relation": "friend", "person": "Jill"},
            {"relation": "tenant", "person": "Nash"}  # 修正：Zalika应该是Nash的租客
        ]
    },
    {
        "name": "John",
        "age": 27,
        "job": "writer",
        "connections": [
            {"relation": "partner", "person": "Jill"},
            {"relation": "cousin", "person": "Nash"}
        ]
    },
    {
        "name": "Nash",
        "age": 34,
        "job": "chef",
        "connections": [
            {"relation": "cousin", "person": "John"},
            {"relation": "landlord", "person": "Zalika"}  # 修正：Nash是Zalika的房东
        ]
    }
]


def find_person(name, group):
    """Find a person by name in the group."""
    for person in group:
        if person["name"] == name:
            return person
    return None


def get_connections(name, group):
    """Get all connections for a person."""
    person = find_person(name, group)
    if person:
        return person.get("connections", [])
    return []


def forget(person1, person2, group):

    for person in group:
        if person["name"] == person1:
            person["connections"] = [conn for conn in person["connections"] if conn["person"] != person2]
        if person["name"] == person2:
            person["connections"] = [conn for conn in person["connections"] if conn["person"] != person1]
    return group

def add_person(name, age, job, relations, group):
    new_person = {
        "name": name,
        "age": age,
        "job": job,
        "connections": relations
    }
    group.append(new_person)
    return group

def average_age(group):
    if not group:
        return 0
    total_age = sum(person["age"] for person in group)
    return total_age / len(group)

if __name__ == "__main__":
    max_age = max(person["age"] for person in my_group)
    print(f"the maximum age of people in the group: {max_age}")

    relation_counts = [len(person.get("connections", [])) for person in my_group]
    avg_relations = sum(relation_counts) / len(relation_counts)
    print(f"the average (mean) number of relations among members of the group: {avg_relations:.1f}")

    ages_with_relations = [person["age"] for person in my_group if len(person.get("connections", [])) > 0]
    max_age_with_relations = max(ages_with_relations) if ages_with_relations else 0
    print(f"the maximum age of people in the group that have at least one relation: {max_age_with_relations}")


    def has_friend(person):
        return any(conn["relation"] == "friend" for conn in person.get("connections", []))


    ages_with_friends = [person["age"] for person in my_group if has_friend(person)]
    max_age_with_friends = max(ages_with_friends) if ages_with_friends else 0
    print(f"the maximum age of people in the group that have at least one friend: {max_age_with_friends}")