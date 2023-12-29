class ContactBook:
    """class to define contact book"""
    def _init_(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email):
        if name not in self.contacts:
            self.contacts[name] = {'phone': phone_number, 'email': email}
            print(f"Contact {name} added successfully.")
        else:
            print(f"Contact {name} already exists.")

    def search_contact(self, query):
        results = []
        for name, contact_info in self.contacts.items():
            if query.lower() in name.lower() or query in contact_info['phone']:
                results.append((name, contact_info['phone'], contact_info['email']))
        return results

    def update_contact(self, name, new_phone_number, new_email):
        if name in self.contacts:
            self.contacts[name]['phone'] = new_phone_number
            self.contacts[name]['email'] = new_email
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

contact_book = ContactBook()

""" Add contacts"""
contact_book.add_contact('John Doe', '123-456-7890', 'john@example.com')
contact_book.add_contact('Jane Smith', '987-654-3210', 'jane@example.com')

"""Search for a contact"""
search_results = contact_book.search_contact('John')
print("Search Results:", search_results)

"""Update a contact"""
contact_book.update_contact('John Doe', '111-222-3333', 'newemail@example.com')

"""Delete a contact"""
contact_book.delete_contact('Jane Smith')

"""Print the updated contact book"""
print("Updated Contact Book:", contact_book.contacts)