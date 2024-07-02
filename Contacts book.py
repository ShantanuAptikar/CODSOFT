class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()

        self.contacts[phone] = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts.values():
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self):
        search = input("Enter name or phone number to search: ").strip()
        for contact in self.contacts.values():
            if contact['name'] == search or contact['phone'] == search:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
                return
        print("Contact not found.")

    def update_contact(self):
        phone = input("Enter the phone number of the contact to update: ").strip()
        if phone in self.contacts:
            print("Enter new details (leave blank to keep current value):")
            name = input(f"New name (current: {self.contacts[phone]['name']}): ").strip() or self.contacts[phone]['name']
            email = input(f"New email (current: {self.contacts[phone]['email']}): ").strip() or self.contacts[phone]['email']
            address = input(f"New address (current: {self.contacts[phone]['address']}): ").strip() or self.contacts[phone]['address']

            self.contacts[phone].update({
                "name": name,
                "email": email,
                "address": address
            })
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self):
        phone = input("Enter the phone number of the contact to delete: ").strip()
        if phone in self.contacts:
            del self.contacts[phone]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def run(self):
        while True:
            print("\nContact Manager")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = ContactManager()
    manager.run()
