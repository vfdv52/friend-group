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


# Example usage
if __name__ == "__main__":
    jill_info = find_person("Jill", my_group)
    print(f"Jill的连接: {get_connections('Jill', my_group)}")

    # 更多示例
    print(f"\nJill的信息: {jill_info}")
    print(f"Zalika的连接: {get_connections('Zalika', my_group)}")