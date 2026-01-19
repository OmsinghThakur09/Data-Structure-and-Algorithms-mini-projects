from route_planner import RoutePlanner


def load_sample_network(planner):
    print("\n🗺️  Loading sample network (Major Indian Cities)...")

    cities = [
        ("Mumbai", 12442373, "India"),
        ("Delhi", 11007835, "India"),
        ("Bangalore", 8443675, "India"),
        ("Hyderabad", 6809970, "India"),
        ("Chennai", 7088000, "India"),
        ("Kolkata", 4496694, "India"),
        ("Pune", 3124458, "India"),
        ("Ahmedabad", 5577940, "India"),
        ("Jaipur", 3046163, "India"),
        ("Nagpur", 2405665, "India"),
        ("Agra", 152001, "India")
    ]

    for city, pop, country in cities:
        planner.add_city(city, pop, country)

    routes = [
        ("Mumbai", "Pune", 150),
        ("Mumbai", "Ahmedabad", 530),
        ("Mumbai", "Nagpur", 785),
        ("Delhi", "Jaipur", 280),
        ("Delhi", "Agra", 230),
        ("Bangalore", "Chennai", 350),
        ("Bangalore", "Hyderabad", 570),
        ("Hyderabad", "Chennai", 625),
        ("Hyderabad", "Nagpur", 500),
        ("Kolkata", "Hyderabad", 1495),
        ("Pune", "Hyderabad", 560),
        ("Ahmedabad", "Jaipur", 660),
        ("Nagpur", "Kolkata", 1050),
        ("Delhi", "Kolkata", 1470)
    ]

    for city1, city2, dist in routes:
        planner.add_route(city1, city2, dist)

    print(f"\nLoaded {len(cities)} cities and {len(routes)} routes!")


def show_menu():
    print("\n" + "-" * 70)
    print("CITY ROUTE PLANNER".center(70))
    print("-" * 70)
    print("  1.  Add City")
    print("  2.  Remove City")
    print("  3.  Add Route")
    print("  4.  Remove Route")
    print("  5.  Show All Cities")
    print("  6.  Show City Routes")
    print("  7.  Check if Route Exists")
    print("  8.  Find Shortest Path (Dijkstra)")
    print("  9.  Find All Paths")
    print(" 10.  Find Nearest Cities")
    print(" 11.  Network Statistics")
    print(" 12.  Load Sample Network")
    print("  0.  Exit")
    print("-" * 70)


def get_input(prompt):
    while True:
        value = input(prompt)
        if value:
            return value
        print("Input cannot be empty!")


def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val and value < min_val:
                print(f"Please enter value > {min_val}")
                continue
            if max_val and value > max_val:
                print(f"Please enter value < {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number!")


def interactive_menu():
    print("\n🗺 Welcome to City Route Planner!")
    planner = RoutePlanner()

    while True:
        show_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":  # Add City
            print("\n--- Add New City ---")
            name = get_input("City name: ")
            pop_input = input("Population (optional): ").strip()
            population = pop_input if pop_input else None
            country = input("Country (optional): ").strip()
            planner.add_city(name, population, country)

        elif choice == "2":  # Remove City
            name = get_input("\nEnter city name to remove: ")
            planner.remove_city(name)

        elif choice == "3":  # Add Route
            print("\n--- Add Route ---")
            city1 = get_input("Enter first city: ")
            city2= get_input("Enter second city: ")
            distance = get_int_input("Distance (km): ", min_val=1)
            planner.add_route(city1,city2, distance)

        elif choice == "4":  # Remove Route
            print("\n--- Remove Route ---")
            city1 = get_input("Enter first city: ")
            city2 = get_input("Enter second city: ")
            planner.remove_route(city1, city2)

        elif choice == "5":  # Show All Cities
            planner.show_all_cities()

        elif choice == "6":  # Show City Routes
            name = get_input("Enter city name: ")
            planner.show_city_routes(name)

        elif choice == "7":  # Check Route Exists
            print("\n--- Check Route ---")
            city1 = get_input("Enter first city: ")
            city2 = get_input("Enter second city: ")
            planner.check_route_exists(city1, city2)

        elif choice == "8":  # Find Shortest Path
            print("\n--- Find Shortest Path (Dijkstra) ---")
            start = get_input("Enter start city: ")
            end = get_input("Enter end city: ")
            planner.find_shortest_path(start, end)

        elif choice == "9":  # Find All Paths
            print("\n--- Find All Paths ---")
            start = get_input("Enter start city: ")
            end = get_input("Enter end city: ")
            max_stops_input = input("Max stops (optional): ").strip()
            max_stops = int(max_stops_input) if max_stops_input else None
            planner.find_all_paths(start,end, max_stops)

        elif choice == "10":  # Find Nearest Cities
            name = get_input("Enter city: ")
            n = get_int_input("How many nearest cities? (default 5): ", min_val=1) or 5
            planner.find_nearest_cities(name, n)

        elif choice == "11":  # Network Statistics
            planner.network_statistics()

        elif choice == "12":  # load sample network
            if planner.network.get_city_count() > 0:
                confirm = input("This will add cities to your current network. continue? (y/n): ")
                if confirm.lower() != "y":
                    continue
            load_sample_network(planner)

        elif choice == "0":  # Exit
            print("\nThank you for using City Route Planner!")
            print("Safe travels!")
            break

        else:
            print("❌ Invalid choice! Please enter a number from the menu.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    interactive_menu()
