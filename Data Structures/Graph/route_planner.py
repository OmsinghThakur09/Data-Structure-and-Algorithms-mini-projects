import heapq

from weightedgraph import Weightedgraph, City


class RoutePlanner:
    def __init__(self):
        self.network = Weightedgraph()

    def add_city(self, name, pop=None, country=None):
        if self.network.city_exists(name):
            print(f"City '{name}' already exists!")
            return False

        city = City(name, pop, country)
        self.network.add_city(city)
        print(f"{city} City added!")
        return True

    def remove_city(self, name):
        if not self.network.city_exists(name):
            print(f"City '{name}' not found!")
            return False

        neighbors = list(self.network.graph[name].keys())
        for neighbor in neighbors:
            self.network.remove_route(name, neighbor)

        del self.network.graph[name]
        del self.network.cities[name]
        print(f"City '{name}' removed!")
        return True

    def add_route(self, city1, city2, distance):
        if city1 == city2:
            print(f"Cannot create route from city to itself!")
            return False

        if not self.network.city_exists(city1):
            print(f"City '{city1}' not found!")
            return False

        if not self.network.city_exists(city2):
            print(f"City '{city2}' not found!")
            return False

        if city2 in self.network.graph[city1]:
            print(f"Route between {city1} and {city2} already exists!")
            return False

        self.network.add_route(city1, city2, distance)
        print(f"Route added: {city1} ↔ {city2} ({distance} km)")
        return True

    def remove_route(self, city1, city2):
        if not self.network.city_exists(city1):
            print(f"City '{city1}' not found!")
            return False

        if not self.network.city_exists(city2):
            print(f"City '{city2}' not found!")
            return False

        if city2 not in self.network.graph[city1]:
            print(f"No Route exists between {city1} and {city2}!")
            return False

        self.network.remove_route(city1, city2)
        print(f"Route removed between: {city1} and {city2}!")
        return True

    def show_all_cities(self):
        cities = self.network.get_all_cities()

        if not cities:
            print(f"No cities in the network yet!")
            return

        print(f"\n{'-' * 70}")
        print(f"All Cities ({len(cities)})")
        print(f"\n{'-' * 70}")

        for i, name in enumerate(sorted(cities), 1):
            city_obj = self.network.cities[name]
            route_count = len(self.network.graph[name])
            print(f"  {i}. {city_obj} - {route_count} route(s)")
        print(f"{'-' * 70}\n")

    def show_city_routes(self, city_name):
        if not self.network.city_exists(city_name):
            print(f"City '{city_name}' not found!")
            return

        routes = self.network.get_neighbors(city_name)
        if not routes:
            print(f"{city_name} has no routes yet!")
            return
        print(f"\n{'-' * 70}")
        print(f"Routes from {city_name} ({len(routes)})")
        print(f"{'-' * 70}")

        for i, (neighbor, distance) in enumerate(sorted(routes.items()), 1):
            city_obj = self.network.cities[neighbor]
            print(f"  {i}. {city_obj.name} - {distance} km")
        print(f"{'-' * 70}\n")

    def check_route_exists(self, city1, city2):
        if not self.network.city_exists(city1):
            print(f"City '{city1}' not found!")
            return

        if not self.network.city_exists(city2):
            print(f"City '{city2}' not found!")
            return

        if city2 in self.network.graph[city1]:
            distance = self.network.graph[city1][city2]
            print(f"Direct route exists: {city1} ↔ {city2} ({distance} km)")
        else:
            print(f"No direct route between {city1} and {city2}")

    def dijkstra(self, start, end):  # finds shortest path between start and end cities by using Dijkstra's algorithm.
        """simply checks neighbor of start city and then neighbors of neighbor cities until end city not found and in
        between it updates the distance from the current city to next city it visits if calculated distance is smaller
        than old distance"""
        if not self.network.city_exists(start):
            print(f"City '{start}' not found!")
            return None

        if not self.network.city_exists(end):
            print(f"City '{end}' not found!")
            return None

        if start == end:
            print(f"⚠️  Start and end are the same city!")
            return None

        distances = {city: float('infinity') for city in
                     self.network.graph}  # we only need those cities which have routes.
        distances[start] = 0
        previous = {city: None for city in self.network.graph}

        pq = [(0, start)]  # priority queue(min heap)
        visited = set()

        while pq:
            current_dist, current_city = heapq.heappop(pq)
            if current_city in visited:
                continue

            visited.add(current_city)
            if current_city == end:
                break

            for neighbor, distance in self.network.graph[current_city].items():
                if neighbor in visited:
                    continue
                new_dist = current_dist + distance
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current_city
                    heapq.heappush(pq, (new_dist, neighbor))  # simply getting the closest city from the current city

        if distances[end] == float('infinity'):
            print(f"No route found between {start} and {end}!")
            return None

        path = []
        current = end
        while current:
            path.append(current)
            current = previous[current]
        path.reverse()  # gives path from end to start city, but we need its reverse.
        return path, distances[end]

    def find_shortest_path(self, start, end):  # find and displays shortest path between two cities.
        result = self.dijkstra(start, end)
        if result is None:
            return

        path, total_dist = result
        print(f"\n{'-' * 70}")
        print(f"Shortest Route: {start} → {end}")
        print(f"{'-' * 70}")
        print(f"Total Distance: {total_dist} km")
        print(f"Number of Stops: {len(path) - 1}")
        print(f"Route:")

        print("->".join(path))
        print(f"{'-' * 70}\n")

    def find_all_paths(self, start, end, max_stops=None):
        if not self.network.city_exists(start):
            print(f"City '{start}' not found!")
            return
        if not self.network.city_exists(end):
            print(f"City '{end}' not found!")
            return
        all_paths = []

        def dfs(current, target, path, distance, visited):
            if current == target:
                return all_paths.append((path.copy(), distance))
            if max_stops and len(path) > max_stops + 1:
                return

            for neighbor, dist in self.network.graph[current].items():
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor)
                    dfs(neighbor, target, path, distance + dist, visited)
                    path.pop()
                    visited.remove(neighbor)

        visited = {start}
        dfs(start, end, [start], 0, visited)

        if not all_paths:
            print(f"No paths found between {start} and {end}!")
            return

        all_paths.sort(key=lambda x: x[1])
        print(f"\n{'=' * 70}")
        print(f"🗺️  All Paths: {start} → {end} ({len(all_paths)} found)")
        print(f"{'=' * 70}")

        for i, (path, distance) in enumerate(all_paths[:10], 1):
            path_str = "->".join(path)
            print(f"{i}. {path_str}")
            print(f"  Distance: {distance} km, Stops: {len(path) - 1}")

        if len(all_paths) > 10:
            print(f"\n.... and {len(all_paths) - 10} more paths")

        print(f"{'-' * 70}\n")

    def find_nearest_cities(self, city_name, n=5):
        if not self.network.city_exists(city_name):
            print(f"City '{city_name}' not found!")
            return

        distances = {city: float('infinity') for city in self.network.graph}
        distances[city_name] = 0

        pq = [(0, city_name)]
        visited = set()

        while pq:
            current_dist, current_city = heapq.heappop(pq)
            if current_city in visited:
                continue

            visited.add(city_name)
            for neighbor, dist in self.network.graph[current_city].items():
                if neighbor in visited:
                    continue

                new_dist = current_dist + dist
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        nearest = [(city, dist) for city, dist in distances.items()
                   if city != city_name and dist != float('infinity')]
        nearest.sort(key=lambda x: x[1])
        nearest = nearest[:n]

        if not nearest:
            print(f"No reachable cities from {city_name}")
            return
        print(f"\n{'-' * 70}")
        print(f"{n if n <= self.network.get_city_count() else self.network.get_city_count() - 1} "
              f"Nearest Cities to {city_name}")
        print(f"{'-' * 70}")

        for i, (city, dist) in enumerate(nearest, 1):
            city_obj = self.network.cities[city]
            print(f"  {i}. {city_obj} - {dist} km away")

        print(f"{'-' * 70}\n")

    def network_statistics(self):
        if not self.network.graph:
            print("No cities in the network!")
            return

        total_cities = self.network.get_city_count()
        total_routes = self.network.get_route_count()

        avg_routes = total_routes / total_cities if total_cities > 0 else 0

        max_connection = max((len(routes) for routes in self.network.graph.values())
                             if self.network.graph else 0)
        most_connected = [city for city, routes in self.network.graph.items()
                          if len(routes) == max_connection]

        print(f"\n{'-' * 70}")
        print(f"Network Statistics")
        print(f"{'=' * 70}")
        print(f"  Total Cities: {total_cities}")
        print(f"  Total Routes: {total_routes}")
        print(f"  Average Routes per City: {avg_routes:.2f}")
        print(f"  Most Connected City: {','.join(most_connected)} ({max_connection} routes)")
        print(f"{'-' * 70}\n")
