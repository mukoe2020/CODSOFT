class ContactBook:
    """Class to define contact book"""

    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email, address=''):
        """Add a new contact to the contact book."""
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone_number, 'email': email, 'address': address}
            print(f"Contact {name} added successfully.")
        else:
            print(f"Contact {name} already exists.")

    def view_contact_list(self):
        """View the list of all contacts in the contact book."""
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("\nContact List:")
            for name, contact_info in self.contacts.items():
                print(f"Name: {name}\nPhone: {contact_info['phone']}\nEmail: {contact_info['email']}\nAddress: {contact_info['address']}\n")

    def search_contact(self, query):
        """Search for a contact by name or phone number."""
        results = []
        for name, contact_info in self.contacts.items():
            if query.lower() in name.lower() or query in contact_info['phone']:
                results.append((name, contact_info['phone'], contact_info['email'], contact_info['address']))
        return results

    def update_contact(self, name, new_phone_number, new_email, new_address=''):
        """Update the details of an existing contact."""
        if name in self.contacts:
            self.contacts[name]['phone'] = new_phone_number
            self.contacts[name]['email'] = new_email
            self.contacts[name]['address'] = new_address
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        """Delete a contact from the contact book."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")


"""Example use: """

contact_book = ContactBook()

while True:
    print("\n1. Add Contact\n2. View Contact List\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address (optional): ")
        contact_book.add_contact(name, phone_number, email, address)

    elif choice == '2':
        contact_book.view_contact_list()

    elif choice == '3':
        query = input("Enter name or phone number to search: ")
        search_results = contact_book.search_contact(query)
        print("Search Results:", search_results)

    elif choice == '4':
        name = input("Enter the name of the contact to update: ")
        new_phone_number = input("Enter the new phone number: ")
        new_email = input("Enter the new email: ")
        new_address = input("Enter the new address (optional): ")
        contact_book.update_contact(name, new_phone_number, new_email, new_address)

    elif choice == '5':
        name = input("Enter the name of the contact to delete: ")
        contact_book.delete_contact(name)

    elif choice == '6':
        print("Exiting the contact book. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose a number from 1 to 6.")
