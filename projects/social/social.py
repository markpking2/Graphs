import sys
sys.path.insert(0, '../graph/')
from itertools import combinations
from functools import reduce
from random import shuffle
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        
        for i in range(1, num_users + 1):
            self.add_user(f'User {i}')

        friendships = list(combinations(range(num_users), 2))
        shuffle(friendships)
        for i in range(num_users * avg_friendships // 2):
            self.add_friendship(friendships[i][0] + 1, friendships[i][1] + 1)

        # Create friendships

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        queue = Queue()
        queue.enqueue([user_id])
        while queue.size() > 0:
            current_path = queue.dequeue()
            current_vertex = current_path[-1]
            if current_vertex not in visited:
                visited[current_vertex] = current_path
                for vertex in self.friendships[current_vertex]:
                    queue.enqueue(current_path + [vertex])
        return visited

    def average_degree_of_separation(self, user_id):
        connections = self.get_all_social_paths(user_id)
        if len(connections) > 1:
            return (reduce(lambda a, b: a + b, [len(connections[c]) for c in connections]) - 1) / (len(connections) - 1)
        else:
            return 0

    def social_network_percentage(self, user_id):
        if len(connections) > 1:
            return len(self.get_all_social_paths(user_id)) / len(self.users) * 100
        else:
            return 0
        



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    # print(connections)
    print(sg.average_degree_of_separation(1))
    print(sg.social_network_percentage(1))
