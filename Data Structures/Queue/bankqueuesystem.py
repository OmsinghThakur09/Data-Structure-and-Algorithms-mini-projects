"""
bank queue management system program to manage and handle bank customers
includes managing different type of customer with different priorities at
multiple counters of the bank.
"""
import heapq
from collections import deque
from datetime import datetime, timedelta

from customer import Customer, Counter


class BankQueueSystem:

    def __init__(self, num_counters=3):
        self.counters = [Counter(i + 1) for i in range(num_counters)]
        self.priority_queue = []  # Min heap priority queue for priority customers
        self.regular_queue = deque()  # normal queue for regular customers
        self.served_customers = []
        self.start_time = datetime.now()

    def add_counter(self):
        new_counter = Counter(len(self.counters)+1)
        self.counters.append(new_counter)
        print(f"Counter {new_counter.id} added!")

    def remove_counter(self):
        if len(self.counters) > 1:
            removed = self.counters.pop()
            if removed.current_customer:
                customer = removed.current_customer
                priority = customer.get_priority()
                if priority == 4:
                    self.regular_queue.appendleft(customer)
                else:
                    heapq.heappush(self.priority_queue, (customer.get_priority, customer.id, customer))
                print(f"Customer: {customer.id} returned to queue")
                print(f"Counter: {removed.id} removed!")
            else:
                print("Cannot remove the last counter")

    def process_queue(self):
        # assigning customers to available counters
        for counter in self.counters:
            if counter.is_available():
                next_customer = self.get_next_customer()
                if isinstance(next_customer, int):
                    break
                else:
                    counter.assign_customer(next_customer)
                    print(f"{next_customer.name} assigned to Counter {counter.id}")

    def get_next_customer(self):
        if self.priority_queue:  # checking priority queue first
            _, _, customer = heapq.heappop(self.priority_queue)
            return customer

        if self.regular_queue:
            return self.regular_queue.popleft()  # then checking regular queue

        return -1

    def add_customer(self, name, service_type, customer_type="Regular"):
        customer = Customer(name, service_type, customer_type)

        if customer_type in ["VIP", "Senior", "Disabled"]:
            # adding to priority queue
            heapq.heappush(self.priority_queue, (customer.get_priority(), customer.id, customer))
            print(f"{customer} added to Priority queue!")

        else:
            self.regular_queue.append(customer)
            print(f"{customer} added to regular queue!")

        self.process_queue()
        return customer

    def get_waiting_customers(self):
        # gives list of all waiting customers
        priority_customers = [c for _, _, c in self.priority_queue]
        regular_customers = list(self.regular_queue)
        return priority_customers + regular_customers

    def get_total_waiting(self):  # returns total no. of waiting customers
        return len(self.priority_queue) + len(self.regular_queue)

    def display_status(self):
        print(f"\n{'-' * 70}")
        print(f"🏦 BANK QUEUE STATUS".center(70))
        print(f"{'-' * 70}")
        print(f"Time: {datetime.now().strftime('%I:%M:%S %p')}")  # (12-hours clock, minutes, seconds, AM or PM)
        print(f"Waiting Customers: {self.get_total_waiting()}")

        print(f"\n--- Service Counters({len(self.counters)}) ---")
        for counter in self.counters:
            status = "🟢" if counter.is_available() else "🔴"
            print(f"{status} {counter}")

        if self.priority_queue:
            print(f"\n--- Priority Queue Customers({len(self.priority_queue)}) ---")
            sorted_priority = sorted(self.priority_queue, key=lambda x: (x[0], x[1]))
            for i, (priority, _, customer) in enumerate(sorted_priority[:5], 1):
                wait_time = customer.get_wait_time()
                print(f"{i}. {customer} - Wait: {wait_time:1f} min")
            if len(self.priority_queue) > 5:
                print(f"....and {len(self.priority_queue) - 5} more")

        if self.regular_queue:
            print(f"\n--- Regular Queue Customers({len(self.regular_queue)}) ---")
            for i, customer in enumerate(self.regular_queue[:5], 1):
                wait_time = customer.get_wait_time()
                print(f"{i}. {customer} - Wait: {wait_time:1f} min")
            if len(self.priority_queue) > 5:
                print(f"....and {len(self.priority_queue) - 5} more")

        print(f"{'-' * 70}\n")

    def complete_all_services(self):
        # complete any finished services
        completed = []
        for counter in self.counters:
            if counter.current_customer and counter.is_available():
                completed.append(counter.current_customer)
                self.served_customers.append((counter.current_customer, counter.id))

        if completed:
            print(f"Completed services:")
            for customer in completed:
                print(f"{customer.name} - Total time: {customer.get_wait_time() + customer.get_service_time():1f} min")

        self.process_queue()

    def simulate_time(self, mins=1):
        # simulates passage of time
        print(f"\nSimulating {mins} minute(s) passing...")
        for counter in self.counters:
            if counter.current_customer:
                if counter.service_end_time:
                    counter.service_end_time -= timedelta(minutes=mins)

        self.complete_all_services()

    def get_statistics(self):
        if not self.served_customers and self.get_total_waiting() == 0:
            print("No data available yet!")
            return

        total_served = len(self.served_customers)
        total_waiting = self.get_total_waiting()

        if self.served_customers:
            avg_wait = sum(customer.get_wait_time() for customer in self.served_customers) / len(self.served_customers)
            max_wait = max(customer.get_wait_time() for customer in self.served_customers)
        else:
            avg_wait = 0
            max_wait = 0

        total_service_time = sum(counter.total_service_time for counter in self.counters)
        elapsed_time = (datetime.now() - self.start_time).total_seconds() / 60  # in minutes

        """utilization = actual hours used / Total available hours * 100. here, actual used time = total_service_time 
        and total available time is how much time bank or system was on board so elapsed time = total available hours *
        no. of counters (because each counter can work independently and simultaneously) """

        utilization = (total_service_time / elapsed_time * len(self.counters)) * 100 if elapsed_time else 0  # in percentage

        print(f"\n{'-' * 70}")
        print(f"BANK STATISTICS".center(70))
        print(f"{'-' * 70}")
        print(f"  Total Customers Served: {total_served}")
        print(f"  Currently Waiting Customers: {total_waiting}")
        print(f"  Average Wait Time: {avg_wait:.2f} minutes")
        print(f"  Maximum Wait Time: {max_wait:.2f} minutes")
        print(f"  Counter Utilization: {utilization:.1f}%")
        print(f"\n--- Per Counter Stats ---")
        for counter in self.counters:
            print(
                f"Counter {counter.id}: {counter.customers_served} served, {counter.total_service_time:.1f} min total")
        print(f"{'-' * 70}\n")

    def find_customer(self, customer_id):
        # checking priority queue
        for _, _, customer in self.priority_queue:
            if customer.id == customer_id:
                return customer, "Priority Queue"

        # checking regular queue
        for customer in self.regular_queue:
            if customer.id == customer_id:
                return customer, "Regular Queue"

        # check counters
        for counter in self.counters:
            if counter.current_customer and counter.current_customer.id == customer_id:
                return counter.current_customer, f"Being served at Counter: {counter.id}"

        # Check served customers
        for customer, id in self.served_customers:
            if customer.id == customer_id:
                return customer, f"Already served at counter: {id}"

        return None, None
