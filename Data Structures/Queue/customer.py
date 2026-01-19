import random
from datetime import datetime, timedelta


class Customer:
    customer_id_counter = 1

    def __init__(self, name, service_type, customer_type="Regular"):
        self.id = Customer.customer_id_counter
        Customer.customer_id_counter += 1
        self.name = name
        self.service_type = service_type  # Deposit, Withdrawal, Loan, acc opening, enquiry, etc.
        self.customer_type = customer_type  # Regular, VIP, Senior, Disabled
        self.arrival_time = datetime.now()
        self.service_start_time = None
        self.service_end_time = None
        self.assigned_counter = None

    def get_priority(self):
        priority_map = {
            "Disabled": 1,
            "VIP": 2,
            "Senior": 2,
            "Regular": 3
        }
        return priority_map.get(self.customer_type, 3)

    def get_service_time(self):
        service_time = {
            "Deposit": random.randint(2, 5),
            "Withdrawal": random.randint(2, 4),
            "Balance Inquiry": random.randint(1, 2),
            "Loan Application": random.randint(15, 20),
            "Account Opening": random.randint(8, 12),
            "Other": random.randint(3, 6)
        }
        return service_time.get(self.customer_type, 3)

    def get_wait_time(self):
        # calculating wait time in minutes
        if self.service_start_time:
            wait = (self.service_start_time - self.arrival_time).total_seconds / 60
            return round(wait, 2)
        else:
            wait = (datetime.now() - self.arrival_time).total_seconds() / 60
            return round(wait, 2)

    def __str__(self):
        return f"#{self.id}, {self.name}, ({self.service_type})"

    def __lt__(self, other):
        return self.get_priority() < other.get_priority()


class Counter:
    # Represents a bank service counter/teller
    def __init__(self, counter_id):
        self.id = counter_id
        self.current_customer = None
        self.service_end_time = None
        self.customers_served = 0
        self.total_service_time = 0

    def complete_service(self):
        if self.current_customer:
            self.current_customer.service_end_time = datetime.now()
            self.customers_served += 1
            self.current_customer = None
            self.service_end_time = None

    def is_available(self):
        if self.current_customer is None:
            return True

        if datetime.now() >= self.service_end_time:
            self.complete_service()
            return True

        return False

    def assign_customer(self, customer):
        self.current_customer = customer
        customer.service_start_time = datetime.now()
        customer.assigned_counter = self.id
        service_duration = customer.get_service_time()
        self.service_end_time = datetime.now() + timedelta(minutes=service_duration)
        self.total_service_time += service_duration

    def get_remaining_time(self):
        if self.current_customer and self.service_end_time:
            remaining = (self.service_end_time - datetime.now()).total_seconds() / 60  # in minutes
            return max(0, round(remaining, 2))
        return 0

    def __str__(self):
        if self.current_customer:
            time_left = self.get_remaining_time()
            return f"Counter {self.id}: Serving {self.current_customer.name} - {time_left:.1f} min left"
        return f"Counter {self.id}: Available"


