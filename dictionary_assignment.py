records={}
while True:
    print("""<----------------Menu------------------->\n
            1.List all records
            2.Add Record
            3.Edit Record
            4.Delete Record
            5.Exit""")
    choice = int(input("Enter your oprtion :"))

    if choice==1:
        if len(records)==0:
            print("oops❗ No Records avilable🥴")
        else:
            for name,info in records.items():
                print(name,info)
    
    elif choice==2:
        name = input("Enter name: ").strip()
        if not name:
            print("⚠️Name cannot be empty")
            continue
        if name in records:
            print("⚠️ Name already exists.")
            continue
        
        p_n = int(input("Enter the number of contact number you like to add :"))
        phone = []
        email = []

        for i in range(0,p_n):
            phone.append(input(f"Enter {i} contact number:"))
        e_n = int(input("Enter the number of e-mail id you like to add :"))

        for i in range(0,e_n):
            email.append(input(f"Enter {i} e-mail : "))
        
        records[name] = {
            "name" : name,
            "phone" : phone,
            "email" : email
        }
        print("Record added succesful✅")

    elif choice == 3:
        key = input("Enter the name to update details : ")

        if key not in records:
            print("Records not found!")
        else:
            print("""\nEdit Options:
            1. Edit Name
            2. Add Phone
            3. Add Email
            4. Delete Phone
            5. Delete Email
            6. Replace Phone
            7. Replace Email""")
            
            edit_choice = int(input("Enter your edit option : "))

            if edit_choice == 1:
                new_name = input("Enter new name: ")
                records[new_name] = records.pop(name)
                print("Name updated succesfully !")
            
            elif edit_choice ==2:
                new_phone = input("Enter new name: ")
                records[name]["phone"].append(new_phone)
                print("Phone added succesfully !")

            elif edit_choice ==3:
                new_mail = input("Enter new name: ")
                records[name]["email"].append(new_mail)
                print("Email added succesfully !")

            elif edit_choice == 4:
                print("Phone Numbers:", records[name]["phone"])
                del_phone = input("Enter phone to delete: ")
                if del_phone in records[name]["phone"]:
                    records[name]["phone"].remove(del_phone)
                    print("Phone deleted.")
                else:
                    print("Phone not found.")
            
            elif edit_choice == 5:
                print("Emails:", records[name]["email"])
                del_email = input("Enter email to delete: ")
                if del_email in records[name]["email"]:
                    records[name]["email"].remove(del_email)
                    print("Email deleted.")
                else:
                    print("Email not found.")
            
            elif edit_choice == 6:
                print("phone Numbers",records[name][phone])
                old = input("Enter old phone to replace : ")
                if old in records[name]["phone"]:
                    new = input("Enter new phone: ")
                    index = records[name]["phone"].index(old)
                    records[name]["phone"][index]=new
                    print("Phone replaced successfully!")
                else:
                    print("Phone not found.")

            # ------ Replace Email ------
            elif edit_choice == 7:
                print("Emails:", records[name]["email"])
                old = input("Enter old email to replace: ")
                if old in records[name]["email"]:
                    new = input("Enter new email: ")
                    index = records[name]["email"].index(old)
                    records[name]["email"][index] = new
                    print("Email replaced successfully!")
                else:
                    print("Email not found.")
            else:
                print("Invalid edit option!")
        
    elif choice == 4:
        del_name = input("Enter the name to delete: ")
        if del_name in records:
            del records[del_name]
            print("Record deleted successfully!")
        else:
            print("Record not found!")

# ---------------- EXIT ---------------- #

    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid input🤥")