import time
from bankqueuesystem import BankQueueSystem


def load_sample_customers(bank):
    print("\nLoading sample customers...")

    customers = [
        ("Sanskar Joshi", "Deposit", "Regular"),
        ("Tejas Kale", "Withdrawal", "VIP"),
        ("Raj Bisen", "Balance Inquiry", "Senior"),
        ("Rohan Pawar", "Loan Application", "Regular"),
        ("Elvish Goenka", "Withdrawal", "Regular"),
        ("Faruk Mistri", "Account Opening", "VIP"),
        ("Gaurav Deshmukh", "Deposit", "Disabled"),
        ("Yash Bais", "Other", "Regular"),
    ]

    for name, service, ctype in customers:
        bank.add_customer(name, service, ctype)
        time.sleep(0.1)  # Small delay for realism

    print(f"\nLoaded {len(customers)} sample customers!")


def show_menu():
    print("\n" + "-"*70)
    print("BANK QUEUE SIMULATION".center(70))
    print("-"*70)
    print("  1.  Add Customer")
    print("  2.  View Current Status")
    print("  3.  Process Queues (Assign to Counters)")
    print("  4.  Complete Services (Check Finished)")
    print("  5.  Simulate Time Passing")
    print("  6.  Find Customer by ID")
    print("  7.  View Statistics")
    print("  8.  Load Sample Customers")
    print("  9.  Add Counter")
    print("  10.  Remove Counter")
    print("  0.  Exit")
    print("-"*70)


def get_input(prompt):
    while True:
        value = input(prompt)
        if value:
            return value
        print("Input cannot be empty!")


def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = input(prompt)
            if min_val is not None and value < min_val:
                print(f"⚠️  Please enter a value >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"⚠️  Please enter a value <= {max_val}")
                continue
            return value
        except ValueError:
            print("⚠️  Please enter a valid number!")


def interactive_menu():
    print("\n🏦 Welcome to Bank Queue Simulation!")

    num_counters = get_int_input("Enter the number of counters(1-10): ", 1, 10)
    bank = BankQueueSystem(num_counters)
    print(f"\nBank initialized with {num_counters} counter(s)!")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":  # Add Customer
            print("\n--- Add New Customer ---")
            name = get_input("Customer name: ")

            print("\nService Types:")
            print("  1. Deposit")
            print("  2. Withdrawal")
            print("  3. Balance Inquiry")
            print("  4. Loan Application")
            print("  5. Account Opening")
            print("  6. Other")
            service_choice = get_int_input("Select services (1-6): ", 1, 6)
            services = ["Deposit", "Withdrawal", "Balance Inquiry", "Loan Application", "Account Opening", "Other"]
            service_type = services[int(service_choice) - 1]

            print("\nCustomer Types:")
            print("  1. Regular")
            print("  2. VIP")
            print("  3. Senior Citizen")
            print("  4. Disabled")
            type_choice = get_int_input("Select type(1-4)", 1, 4)
            types = ["Regular", "VIP", "Senior", "Disabled"]
            customer_type = types[int(type_choice) - 1]

            bank.add_customer(name, service_type, customer_type)

        elif choice == "2":  # View Status
            bank.display_status()

        elif choice == "3":  # Process Queues
            print("\nProcessing queues...")
            bank.process_queue()
            bank.display_status()

        elif choice == "4":  # Complete Services
            print("\n✅ Checking for completed services...")
            bank.complete_all_services()

        elif choice == "5":  # Simulate Time
            min = get_int_input("How many minutes to simulate?(1-30): ", 1, 30)
            bank.simulate_time(min)
            bank.display_status()

        elif choice == "6":  # Find Customer
            customer_id = get_int_input("\nEnter customer ID: ", min_val=1)
            customer, location = bank.find_customer(customer_id)
            if customer:
                print(f"Found: {customer}")
                print(f"Location: {location}")
                print(f"Wait Time: {customer.get_wait_time():.1f} minutes")

            else:
                print(f"Customer #{customer_id} not found!")

        elif choice == "8":  # Load Sample
            if bank.get_total_waiting() > 0:
                confirm = input("\n⚠This will add customers to current queue. Continue? (y/n): ")
                if confirm.lower() != 'y':
                    continue
            load_sample_customers(bank)

        elif choice == "9":  # Add Counter
            bank.add_counter()
            print(f"\nCurrent counters: {len(bank.counters)}")

        elif choice == "10":  # Remove Counter
            bank.remove_counter()
            print(f"\nCurrent counters: {len(bank.counters)}")

        elif choice == "0":  # Exit
            print("\n👋 Thank you for using Bank Queue Simulation!")
            print("🏦 Have a great day!")
            break

        else:
            print("❌ Invalid choice! Please enter a number from the menu.")


if __name__ == "__main__":
    interactive_menu()
