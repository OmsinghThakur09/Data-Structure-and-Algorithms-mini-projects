# program to analyse social network of users
"""
in this program we cna add, remove user from the network, add friendships, find mutual friends, find connection path
between two user, detect friend circles, and we can show friend stats.
"""
from collections import deque
from graph import Graph, User


class SocialNetwork:
    def __init__(self):
        self.network = Graph()

    def add_user(self, username, age):
        if self.network.find_vertex(username):
            print(f"User already found!")
            return False

        user = User(username, age)
        self.network.add_vertex(user)  # each user will be the vertex of our graph network
        print(f"{user} added!")
        return True

    def remove_user(self, username):
        if not self.network.find_vertex(username):
            print(f"User {username} not found!")
            return False

        friends = self.network.graph[username]
        for friend in friends:
            self.network.remove_edge(username, friend)

        del self.network.graph[username]
        del self.network.users[username]
        print(f"User {username} removed!")
        return True

    def add_friendship(self, user1, user2):
        if user1 == user2:
            print("Users cannot be friends with themselves!")
            return False

        if not self.network.find_vertex(user1):
            print(f"Please add {user1} first! and then try to add friendship")
            return False

        if not self.network.find_vertex(user2):
            print(f"Please add {user2} first! and then try to add friendship")
            return False

        if user2 in self.network.graph[user1]:
            print(f"{user1} and {user2} are already friends!")
            return False

        self.network.add_edges(user1, user2)
        print(f"Friendship added between {user1} and {user2}")
        return True

    def remove_friendship(self, user1, user2):
        if not self.network.find_vertex(user1):
            print(f"User {user1} not found!")
            return False

        if not self.network.find_vertex(user2):
            print(f"User {user2} not found!")
            return False

        if user2 not in self.network.graph[user1]:
            print(f"{user1} and {user2} are not friends!")
            return False

        self.network.remove_edge(user1, user2)
        print(f"Friendship removed between {user1} and {user2}")
        return True

    def show_users_friends(self, username):
        if not self.network.find_vertex(username):
            print(f"{username} not found!")
            return

        friends = self.network.get_neighbor(username)
        if not friends:
            print(f"{username} has no friends yet.")
            return

        print(f"\n{'-' * 70}")
        print(f"{username}'s Friends ({len(friends)})")
        print(f"{'-' * 70}")

        for i, friend in enumerate(friends):
            user_obj = self.network.users[friend]
            print(f" {i}. {user_obj}")

        print(f"{'-' * 70}")

    def show_all_users(self):
        users = self.network.get_all_users()
        if not users:
            print("No users in the network yet!")
            return

        print(f"{'-' * 70}")
        print(f"All Users ({len(users)})")
        print(f"{'-' * 70}")

        for i, username in enumerate(users):
            user_obj = self.network.users[username]
            friend_count = len(self.network.graph[username])
            print(f"  {i}. {user_obj}({friend_count} friend(s))")

        print(f"{'-' * 70}")

    def check_friendship(self, user1, user2):
        if not self.network.find_vertex(user1):
            print(f"User '{user1}' not found!")
            return

        if not self.network.find_vertex(user2):
            print(f"User '{user2}' not found!")
            return

        if user2 in self.network.graph[user1]:
            print(f"{user1} and {user2} are friends!")
        else:
            print(f"{user1} and {user2} are NOT friends.")

    def find_mutual(self, user1, user2):
        if not self.network.find_vertex(user1):
            print(f"{user1} not found!")
            return
        elif not self.network.find_vertex(user2):
            print(f"{user2} not found!")
            return

        friends1 = set(self.network.graph[user1])
        friends2 = set(self.network.graph[user2])
        mutual = friends1.intersection(friends2)

        if not mutual:
            print(f"{user1} and {user2} have no mutual friends!")
            return

        print(f"\n{'-' * 70}")
        print(f"Mutual Friends: {user1} & {user2} ({len(mutual)})")
        print(f"{'-' * 70}")

        for i, friend in enumerate(sorted(mutual), 1):
            user_obj = self.network.users[friend]
            print(f"  {i}. {user_obj}")

        print(f"{'-' * 70}\n")

    def mutual_count(self, user1, user2): # helper function
        if len(self.network.graph[user1]) > len(self.network.graph[user2]):
            mutual_list = [user for user in self.network.graph[user2] if user in self.network.graph[user1]]
        else:
            mutual_list = [user for user in self.network.graph[user1] if user in self.network.graph[user2]]
        return len(mutual_list)

    def suggest_friends(self, username):
        if not self.network.find_vertex(username):
            print(f"user '{username}' not found!")
            return

        suggestion_list = []
        for user in self.network.graph.keys():
            if user == username or user in self.network.graph[username]:
                continue
            mutual = self.mutual_count(username, user)
            if mutual > 0:
                suggestion_list.append((user, mutual))

        if not suggestion_list:
            print(f"No friend suggestions for {username} at the moment.")
            return

        suggestion_list = sorted(suggestion_list, key=lambda item: item[1], reverse=True)

        print("\n" + "-"*70)
        print(f"Friend Suggestions for {username}")
        print("\n" + "-"*70)

        for i, (user, mutual) in enumerate(suggestion_list):
            user_obj = self.network.users[user]
            plural = "friends" if mutual > 1 else "friend"
            print(f" {i}.{user_obj} ({mutual} mutual {plural})")
        print("\n" + "-"*70)

    def connection_path(self, start_u, end_u):
        if not self.network.find_vertex(start_u):
            print(f"{start_u} not found!")
            return

        if not self.network.find_vertex(end_u):
            print(f"{end_u} not found!")
            return

        if start_u == end_u:
            print(f"Same user!")
            return

        visited = set()
        queue = deque([(start_u, [start_u])])
        visited.add(start_u)

        while queue:
            current, path = queue.popleft()
            if current == end_u:  # path found!
                print("\n"+"-"*70)
                print(f"Connection path:{start_u} -> {end_u}")
                print(f"Degrees of Separation: {len(path) - 1}")
                print(f"path: {'->'.join(path)}")
                print("\n"+"-"*70)
                return path

            for neighbor in self.network.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        print(f"No connection path found between {start_u} and {end_u}.")
        return None

    def find_friend_circles(self):
        visited = set()
        circles = []

        def dfs(user, circle):
            visited.add(user)
            circle.append(user)

            for neighbor in self.network.graph[user]:
                if neighbor not in visited:
                    dfs(neighbor, circle)

        for user in self.network.graph:
            if user not in visited:
                circle = []
                dfs(user, circle)
                circles.append(circle)

        print(f"\n{'-' * 70}")
        print(f"🔍 Friend Circles/Communities ({len(circles)})")
        print(f"{'-' * 70}")
        for i, circle in enumerate(circles):
            print(f"\nCircle {i} ({len(circle)} members):")
            for user in sorted(circle):
                user_obj = self.network.users[user]
                print(f"  • {user_obj}")

        print(f"\n{'='*70}\n")

    def most_popular_user(self):
        if not self.network.graph:
            print("No users in the network!")
            return

        max_friends = max(len(friends) for friends in self.network.graph.values())  # finding out the count of maximum friends a user have
        popular_users = [user for user, friends in self.network.graph.items() if len(friends) == max_friends]

        print(f"\n{'-' * 70}")
        print(f"🌟 Most Popular User(s)")
        print(f"{'-' * 70}")

        for user in popular_users:
            user_obj = self.network.users[user]
            print(f"  {user_obj} - {max_friends} friend(s)")
        print(f"{'-' * 70}\n")

    def network_statistics(self):
        if not self.network.graph:
            print("No users in the network!")
            return

        total_users = self.network.get_all_users()
        total_friendships = self.network.get_friendship_count()
        avg_friends = total_friendships / len(total_users) if len(total_users) > 0 else 0

        print(f"\n{'-' * 70}")
        print(f"Network Statistics:")
        print(f"{'-' * 70}")
        print(f"  Total Users: {total_users}")
        print(f"  Total Friendships: {total_friendships}")
        print(f"  Average Friends per User: {avg_friends:.2f}")
        print(f"{'-' * 70}\n")
