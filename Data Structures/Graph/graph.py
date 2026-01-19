# implementation of graph data structure
from collections import deque


class User:
    def __init__(self, username, age, interests=None):
        self.username = username
        self.age = age

    def __str__(self):
        return f"{self.username} ({self.age})"

    def __repr__(self):
        return f"User('{self.username}', {self.age})"


class Graph:
    def __init__(self):
        self.graph = {}
        self.users = {}

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        result = "\n".join([f"{node}: {neighbor} " for node, neighbor in self.graph.items()])
        return result

    def add_vertex(self, user):
        if user.username not in self.graph:
            self.graph[user.username] = []
            self.users[user.username] = user
            return True
        return False

    def add_edges(self, user1, user2):
        if user1 in self.graph and user2 in self.graph:
            if user2 not in self.graph[user1]:
                self.graph[user1].append(user2)
                self.graph[user2].append(user1)
                return True
        return False

    def remove_edge(self,user1,user2):
        if user1 in self.graph and user2 in self.graph:
            if user2 in self.graph[user1]:
                self.graph[user1].remove(user2)
                self.graph[user2].remove(user1)
                return True
        return False

    def find_vertex(self, username):
        return username in self.graph

    def get_neighbor(self, username):
        return self.graph.get(username, [])

    def get_all_users(self):
        return list(self.graph.keys())

    def get_user_count(self):
        return len(self.graph)

    def get_friendship_count(self):
        total = sum(len(friends) for friends in self.graph.values())
        return total // 2  # undirected graph counts each edge two times.

    def bfs(self, start, end=None):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:

            current = queue.popleft()
            print(current, end=' ')
            if end:
                if current == end:
                    break
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, start):
        visited = set()
        stack = [start]
        visited.add(start)

        while stack:
            current = stack.pop()
            print(current, end = ' ')

            for neighbor in reversed(self.graph[current]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)



