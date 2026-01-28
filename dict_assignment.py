records = {}

while True:
    print("""\n<---------------- Menu ------------------->
    1. List all records
    2. Add Record
    3. Edit Record
    4. Delete Record
    5. Exit
    """)

    choice = int(input("Enter your choice: "))

    # ------------------- LIST ALL ---------------------
    if choice == 1:
        if not records:
            print("Oops❗ No records available 😕")
        else:
            print("\n----- All Records -----")
            for name, info in records.items():
                print(f"\nName : {name}")
                print("Phones:", ", ".join(info["phone"]))
                print("Emails:", ", ".join(info["email"]))

    # ------------------- ADD RECORD -------------------
    elif choice == 2:
        name = input("Enter name: ").strip()
        if not name:
            print("⚠️ Name cannot be empty")
            continue

        if name in records:
            print("⚠️ Name already exists.")
            continue

        # Add Phones
        phone = []
        while True:
            ph = input("Enter Phone number (+91XXXXXXXXXX): ").strip()
            if ph.startswith("+91") and len(ph) == 13 and ph[3:].isdigit():
                if ph not in phone:
                    phone.append(ph)
                else:
                    print("This number already exists ⚠️")
            else:
                print("Invalid! Must be +91 followed by 10 digits.")

            if int(input("Add more phone? 1-Yes / 0-No: ")) == 0:
                break

        # Add Emails
        email = []
        while True:
            em = input("Enter email id: ")
            if em.endswith("@gmail.com"):
                
                if em not in email:
                    email.append(em)
                else:
                    print("Email already exists ⚠️")
            else:
                print("Invalid! Must end with @gmail.com")

            if int(input("Add more email? 1-Yes / 0-No: ")) == 0:
                break

        records[name] = {
            "name": name,
            "phone": phone,
            "email": email
        }

        print("Record added successfully 👍")

    # ------------------- EDIT RECORD -------------------
    elif choice == 3:

        name = input("Enter name to edit: ").strip()

        if name not in records:
            print(f"No records found for {name} ⚠️")
            continue

        while True:
            print("""\nEdit Options:
            1. Edit Name
            2. Add Phone
            3. Add Email
            4. Edit Phone
            5. Edit Email
            0. Back to Main Menu
            """)

            edit_choice = int(input("Enter your edit option: "))

            # 1. EDIT NAME
            if edit_choice == 1:
                new_name = input("Enter new name: ").strip()
                if not new_name:
                    print("Name cannot be empty ⚠️")
                    continue

                if new_name in records and new_name != name:
                    print("Name already exists ⚠️")
                    continue

                data = records.pop(name)
                data["name"] = new_name
                records[new_name] = data
                name = new_name

                print("Name updated successfully 👍")

            # 2. ADD PHONE
            elif edit_choice == 2:
                ph = input("Enter new phone (+91XXXXXXXXXX): ").strip()
                if ph.startswith("+91") and len(ph) == 13 and ph[3:].isdigit():
                    if ph not in records[name]["phone"]:
                        records[name]["phone"].append(ph)
                        print("Phone added! 👍")
                    else:
                        print("Phone already exists!")
                else:
                    print("Invalid phone!")

            # 3. ADD EMAIL
            elif edit_choice == 3:
                em = input("Enter new email: ").strip().lower()
                if em.endswith("@gmail.com"):
                    if em not in records[name]["email"]:
                        records[name]["email"].append(em)
                        print("Email added! 👍")
                    else:
                        print("Email already exists!")
                else:
                    print("Invalid email format!")

            # 4. EDIT PHONE
            elif edit_choice == 4:
                print("Phones:", records[name]["phone"])
                old = input("Enter old phone to replace: ").strip()

                if old in records[name]["phone"]:
                    new = input("Enter new phone: ").strip()
                    if new.startswith("+91") and len(new) == 13 and new[3:].isdigit():
                        records[name]["phone"][records[name]["phone"].index(old)] = new
                        print("Phone updated! 👍")
                    else:
                        print("Invalid new phone!")
                else:
                    print("Phone not found!")

            # 5. EDIT EMAIL
            elif edit_choice == 5:
                print("Emails:", records[name]["email"])
                old = input("Enter old email to replace: ").strip().lower()

                if old in records[name]["email"]:
                    new = input("Enter new email: ").strip().lower()
                    if new.endswith("@gmail.com") and "@" in new[:-10]:
                        records[name]["email"][records[name]["email"].index(old)] = new
                        print("Email updated! 👍")
                    else:
                        print("Invalid new email!")
                else:
                    print("Email not found!")

            elif edit_choice == 0:
                break

            else:
                print("Invalid option!")

    # ------------------- DELETE RECORD -------------------
    elif choice == 4:
        name = input("Enter name to delete: ").strip()

        if name not in records:
            print("Record not found ⚠️")
            continue

        while True:
            print("""\nDelete Options:
            1. Delete Entire Record
            2. Delete Phone
            3. Delete Email
            0. Exit
            """)

            delete_choice = int(input("Enter your choice: "))

            # DELETE WHOLE RECORD
            if delete_choice == 1:
                confirm = input("Type 'delete' to confirm: ")
                if confirm == "delete":
                    del records[name]
                    print("Record deleted successfully 👍")
                    break
                else:
                    print("Cancelled!")

            # DELETE PHONE
            elif delete_choice == 2:
                print("Phones:", records[name]["phone"])
                ph = input("Enter phone to delete: ").strip()

                if ph in records[name]["phone"]:
                    confirm = input("Type 'delete' to confirm: ")
                    if confirm == "delete":
                        records[name]["phone"].remove(ph)
                        print("Phone deleted! 👍")
                else:
                    print("Phone not found!")

            # DELETE EMAIL
            elif delete_choice == 3:
                print("Emails:", records[name]["email"])
                em = input("Enter email to delete: ").strip().lower()

                if em in records[name]["email"]:
                    confirm = input("Type 'delete' to confirm: ")
                    if confirm == "delete":
                        records[name]["email"].remove(em)
                        print("Email deleted! 👍")
                else:
                    print("Email not found!")

            elif delete_choice == 0:
                break

            else:
                print("Invalid choice!")

    # ------------------- EXIT -------------------
    elif choice == 5:
        print("Exiting... Thank You 😊")
        break

    else:
        print("Invalid Choice! 🤥")
