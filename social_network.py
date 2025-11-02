class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
    '''
    
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
        else:
            print(f"{friend.name} is already a friend of {self.name}.")


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name in self.people:
            print(f"{name} already exists in the network.")
        else:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people:
            print(f"Error: {person1_name} does not exist in the network.")
            return
        if person2_name not in self.people:
            print(f"Error: {person2_name} does not exist in the network.")
            return
        person1 = self.people[person1_name]
        person2 = self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for person in self.people.values():
            friends_names = [friend.name for friend in person.friends]
            print(f"{person.name}: {', '.join(friends_names) if friends_names else 'No friends'}")


# Test the Social Network

network = SocialNetwork()

# Adding people
people_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
for name in people_names:
    network.add_person(name)

# Adding friendships (at least 8)
friendships = [
    ("Alice", "Bob"),
    ("Alice", "Charlie"),
    ("Bob", "Diana"),
    ("Charlie", "Diana"),
    ("Charlie", "Eve"),
    ("Diana", "Frank"),
    ("Eve", "Frank"),
    ("Alice", "Frank")
]

for p1, p2 in friendships:
    network.add_friendship(p1, p2)

# Edge cases
network.add_person("Alice")  # Duplicate person
network.add_friendship("Alice", "George")  # Person does not exist

# Print the network
network.print_network()


# ------------------------------
# Design Memo (200-300 words)
# ------------------------------
'''
Design Memo:

Using a graph is the ideal structure for modeling a social network because people (nodes)
can have multiple connections (edges) that are not strictly hierarchical or sequential. Unlike
lists or trees, which impose a linear or branching order, a graph allows any person to be
connected to any other person directly, reflecting the complex and non-linear relationships
of real-world social networks.

A list would not efficiently represent friendships because it only allows linear relationships,
making it cumbersome to find or traverse connections. Trees are hierarchical and restrict
each node to one parent, which does not reflect the mutual and multi-directional nature of friendships.

The adjacency list approach used in the SocialNetwork class provides efficient
storage and access for each person's friends. Adding a friendship involves simple list
operations, which are fast, and printing the network only requires iterating over the dictionary
and each person's friend list. The trade-offs include slightly higher memory usage for the
lists within each node and the need to check for duplicates when adding friends. However,
these trade-offs are minimal compared to the flexibility and clarity gained in representing
complex relationships.

Overall, using a graph allows accurate modeling of social connections, easy addition of new
people and friendships, and straightforward traversal or display of the network.
'''