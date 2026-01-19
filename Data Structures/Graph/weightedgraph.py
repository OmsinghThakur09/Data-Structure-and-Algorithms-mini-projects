from collections import defaultdict


class City:
    def __init__(self, name, population=None, country=None):
        self.name = name
        self.population = population
        self.country = country

    def __str__(self):
        if self.population and self.country:
            return f"{self.name} ({self.country}, population: {self.population:})"
        return f"{self.name}"

    def __repr__(self):
        return f"'{self.name}' city"


class Weightedgraph:
    def __init__(self):
        self.graph = defaultdict(dict)  # graph key:city name, values: dictionary(key: city_name, value: distance)
        self.cities = {}  # keys: city_name, values: city objects

    def add_city(self, city):
        if city.name not in self.cities:
            self.cities[city.name] = city
            if city.name not in self.graph:
                self.graph[city.name] = {}
                return True
        return False

    def city_exists(self, city):
        return city in self.cities

    def add_route(self, city1, city2, distance):
        if city1 in self.graph and city2 in self.graph:
            self.graph[city1][city2] = distance
            self.graph[city2][city1] = distance
            return True
        return False

    def remove_route(self, city1, city2):
        if city1 in self.graph and city2 in self.graph:
            del self.graph[city1][city2]
            del self.graph[city2][city1]
            return True
        return False

    def get_neighbors(self, city_name):
        return self.graph.get(city_name, {})

    def get_all_cities(self):
        return list(self.cities.keys())

    def get_city_count(self):
        return len(self.cities)

    def get_route_count(self):
        total = sum(len(routes) for routes in self.graph.values())
        return total // 2  # routes are bidirectional


if __name__ == "__main__":
    planner = Weightedgraph()
    Goa = City("Goa", 400000, "India")
    planner.add_city(Goa)
    print(planner.graph)
    print(planner.cities)

