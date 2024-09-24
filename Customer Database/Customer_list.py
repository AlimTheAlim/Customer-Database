import os
import shelve

class Customer:
    """
    Class representing a single customer with attributes name, email, and phone.
    """

    def __init__(self, name='Dummy', email='DummyEmail', phone='DummyPhone'):
        """
        Initialize a Customer object with optional name, email, and phone parameters.
        """
        self.name = name
        self.email = email
        self.phone = phone

    def set_customer(self, name, email, phone):
        """
        Set the customer's name, email, and phone.
        """
        self.name = name
        self.email = email
        self.phone = phone
        
    def get_customer_name(self):
        """
        Get the customer's name.
        """
        return self.name
    
    def get_customer_phone(self):
        """
        Get the customer's phone number.
        """
        return self.phone
    
    def get_customer_email(self):
        """
        Get the customer's email address.
        """
        return self.email


class Customer_list:
    """
    Class representing a list of customers.
    """
    
    def __init__(self):
        """
        Initialize an empty list to store customers.
        """
        self.customer_list = []
        self.filename = "customer_base.txt"
        if os.path.exists(self.filename):
            self.load_from_file()

    def add_customer(self, customer):
        """
        Add a customer to the customer list.
        """
        self.customer_list.append(customer)
        self.save_to_file()

    def remove_customer(self, customer):
        """
        Remove a customer from the customer list.
        """
        self.customer_list.remove(customer)
        self.save_to_file()

    def edit_customer(self, customer, name=None, email=None, phone=None):
        """
        Edit a customer's information.
        """
        if name:
            customer.name = name
        if email:
            customer.email = email
        if phone:
            customer.phone = phone
        self.save_to_file()

    def print_customer_list(self):
        """
        Print the list of customers.
        """
        for customer in self.customer_list:
            print(f"Name: {customer.get_customer_name()}, Email: {customer.get_customer_email()}, Phone: {customer.get_customer_phone()}")

    def save_to_file(self):
        """
        Save the customer list to the file.
        """
        with open(self.filename, 'w') as file:
            for customer in self.customer_list:
                file.write(f"{customer.get_customer_name()} {customer.get_customer_phone()} {customer.get_customer_email()}\n")

    def load_from_file(self):
        """
        Load the customer list from the file.
        """
        with open(self.filename, 'r') as file:
            for line in file:
                name, phone, email = line.strip().split()
                self.customer_list.append(Customer(name, email, phone))
