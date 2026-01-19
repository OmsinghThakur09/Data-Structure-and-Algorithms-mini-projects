from social_network import SocialNetwork
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_sample_network(social_network):
    print("\nLoading sample network...")

    users = [
        ("Aman", 25),
        ("Bhavesh", 28),
        ("Chaitanya", 30),
        ("Dhiraj", 27),
        ("Yogesh", 24),
        ("Faruk", 29),
        ("Gaurav", 26),
        ("Harish", 31)
    ]

    for username, age in users:
        social_network.add_user(username, age)

    friendships = [
        ("Aman", "Bhavesh"),
        ("Aman", "Chaitanya"),
        ("Bhavesh", "Dhiraj"),
        ("Bhavesh", "Faruk"),
        ("Chaitanya", "Yogesh"),
        ("Dhiraj", "Faruk"),
        ("Dhiraj", "Gaurav"),
        ("Yogesh", "Harish"),
        ("Faruk", "Gaurav"),
        ("Gaurav", "Harish")
    ]
    for user1, user2 in friendships:
        social_network.add_friendship(user1, user2)

    print(f"\nLoaded {len(users)} users and {len(friendships)} friendships!")


def show_menu():
    print("SOCIAL NETWORK ANALYZER".center(70, '-'))
    print("  1.  Add User")
    print("  2.  Remove User")
    print("  3.  Add Friendship")
    print("  4.  Remove Friendship")
    print("  5.  Show User's Friends")
    print("  6.  Show All Users")
    print("  7.  Check if Two Users are Friends")
    print("  8.  Find Mutual Friends")
    print("  9.  Suggest Friends")
    print(" 10.  Find Connection Path")
    print(" 11.  Find Friend Circles")
    print(" 12.  Most Popular User")
    print(" 13.  Network Statistics")
    print(" 14.  Load Sample Network")
    print("  0.  Exit")
    print("-" * 70)


def get_input(prompt):
    while True:
        value = input(prompt)
        if value:
            return value
        print("Input cannot be empty!")


def get_int_input(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value and value < min_value:
                print(f"Please enter value >= {min_value}!")
                continue
            if max_value and value > max_value:
                print(f"Please enter value <= {max_value}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number")


def interactive_menu():
    print("\n🌐 Welcome to Social Network Analyzer!")
    social_network = SocialNetwork()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':  # Add User
            print("\n--- Add New User ---")
            username = get_input("Username: ")
            age = get_int_input("Age: ", 1, 100)
            social_network.add_user(username, age)

        elif choice == '2':  # Remove User
            print("\n--- Remove user ---")
            username = get_input("Enter username: ")
            social_network.remove_user(username)

        elif choice == "3":  # Add Friendship
            print("\n--- Add Friendship ---")
            user1 = get_input("First user:")
            user2 = get_input("Second user:")
            social_network.add_friendship(user1, user2)

        elif choice == "4":  # Remove Friendship
            print("\n--- Remove Friendship ---")
            user1 = get_input("First user:")
            user2 = get_input("Second user:")
            social_network.remove_friendship(user1, user2)

        elif choice == "5":  # Show User's Friends
            username = get_input("Enter username: ")
            social_network.show_users_friends(username)

        elif choice == "6":  # Show All Users
            social_network.show_all_users()

        elif choice == "7":  # Check Friendship
            print("\n--- Check Friendship ---")
            user1 = get_input("First user: ")
            user2 = get_input("Second user: ")
            social_network.check_friendship(user1, user2)

        elif choice == "8":  # Find Mutual Friends
            print("\n--- Find Mutual Friends ---")
            user1 = get_input("First user: ")
            user2 = get_input("Second user: ")
            social_network.find_mutual(user1, user2)

        elif choice == "9":  # Suggest Friends
            username = get_input("\nEnter username: ")
            social_network.suggest_friends(username)

        elif choice == "10":  # Find Connection Path
            print("\n--- Find Connection Path ---")
            user1 = get_input("Enter start user: ")
            user2 = get_input("Enter end user: ")
            social_network.connection_path(user1, user2)

        elif choice == "11":  # Find Friend Circles
            social_network.find_friend_circles()

        elif choice == "12":  # Most Popular User
            social_network.most_popular_user()

        elif choice == "13":  # Network Statistics
            social_network.network_statistics()

        elif choice == "14":  # Load Sample Network
            if social_network.network.get_user_count() > 0:
                confirm = input("\nThis will add users to your current network. Continue? (y/n): ")
                if confirm == 'y':
                    continue
            load_sample_network(social_network)

        elif choice == "0":  # Exit
            print("\nThank you for using Social Network Analyzer!")
            print("Stay connected!")
            break

        else:
            print("❌ Invalid choice! Please enter a number from the menu.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    interactive_menu()
