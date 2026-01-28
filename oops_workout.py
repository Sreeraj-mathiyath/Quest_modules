class Contact:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.emails = []

    def add_phone(self, phone):
        if phone.startswith("+91") and len(phone) == 13 and phone[3:].isdigit():
            if phone not in self.phones:
                self.phones.append(phone)
                return True
        return False

    def add_email(self, email):
        if email.endswith("@gmail.com"):
            if email not in self.emails:
                self.emails.append(email)
                return True
        return False

    def edit_phone(self, old, new):
        if old in self.phones:
            if new.startswith("+91") and len(new) == 13 and new[3:].isdigit():
                self.phones[self.phones.index(old)] = new
                return True
        return False

    def edit_email(self, old, new):
        if old in self.emails:
            if new.endswith("@gmail.com"):
                self.emails[self.emails.index(old)] = new
                return True
        return False


class ContactManager:
    def __init__(self):
        self.records = {}

    def add_contact(self, name):
        if name in self.records:
            print("⚠️ Contact already exists!")
            return None
        contact = Contact(name)
        self.records[name] = contact
        return contact

    def list_contacts(self):
        if not self.records:
            print("No records found 😕")
            return

        for name, c in self.records.items():
            print(f"\nName : {c.name}")
            print("Phones:", ", ".join(c.phones))
            print("Emails:", ", ".join(c.emails))

    def delete_contact(self, name):
        if name in self.records:
            del self.records[name]
            print("Contact deleted 👍")
        else:
            print("Contact not found!")

    def edit_name(self, old, new):
        if old not in self.records:
            print("Contact not found!")
            return

        if new in self.records:
            print("New name already exists!")
            return

        c = self.records.pop(old)
        c.name = new
        self.records[new] = c
        print("Name updated 👍")




#---------------------------------------------------------


cm = ContactManager()

while True:
    print("""\n<---------------- Menu ------------------->
    1. List all records
    2. Add Record
    3. Edit Record
    4. Delete Record
    5. Exit
    """)

    choice = int(input("Enter your choice: "))

    # LIST
    if choice == 1:
        cm.list_contacts()

    # ADD
    elif choice == 2:
        name = input("Enter name: ").strip()
        contact = cm.add_contact(name)
        if not contact:
            continue

        # Add phones
        while True:
            ph = input("Enter phone (+91XXXXXXXXXX): ")
            if contact.add_phone(ph):
                print("Phone added 👍")
            else:
                print("Invalid or duplicate phone!")

            if input("Add more? (y/n): ").lower() != "y":
                break

        # Add emails
        while True:
            em = input("Enter email (@gmail.com): ")
            if contact.add_email(em):
                print("Email added 👍")
            else:
                print("Invalid or duplicate email!")

            if input("Add more? (y/n): ").lower() != "y":
                break

    # EDIT
    elif choice == 3:
        name = input("Enter name to edit: ")
        if name not in cm.records:
            print("Contact not found!")
            continue

        contact = cm.records[name]

        print("""
        1. Edit Name
        2. Add Phone
        3. Add Email
        4. Edit Phone
        5. Edit Email
        """)

        ec = int(input("Enter edit option: "))

        if ec == 1:
            new = input("Enter new name: ")
            cm.edit_name(name, new)

        elif ec == 2:
            ph = input("Enter new phone: ")
            if contact.add_phone(ph):
                print("Phone added 👍")
            else:
                print("Invalid or duplicate phone!")

        elif ec == 3:
            em = input("Enter new email: ")
            if contact.add_email(em):
                print("Email added 👍")
            else:
                print("Invalid or duplicate email!")

        elif ec == 4:
            old = input("Old phone: ")
            new = input("New phone: ")
            if contact.edit_phone(old, new):
                print("Phone updated 👍")
            else:
                print("Invalid or not found!")

        elif ec == 5:
            old = input("Old email: ")
            new = input("New email: ")
            if contact.edit_email(old, new):
                print("Email updated 👍")
            else:
                print("Invalid or not found!")

    # DELETE
    elif choice == 4:
        name = input("Enter name to delete: ")
        cm.delete_contact(name)

    # EXIT
    elif choice == 5:
        print("Exiting... Thank you 😊")
        break

    else:
        print("Invalid choice!")
