from tkinter import *

root = Tk()
back_ground = PhotoImage(file=r"D:\Quest\Tkinter\download (3).png")
root.geometry("800x500")
root.config(bg="white")


bg_label = Label(root, image=back_ground)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

main_frame = Frame(root)
main_frame_label = Label(main_frame, image=back_ground)
main_frame.place(relx=0.5, rely=0.5, anchor="center")
main_frame_label.place(x=0, y=0, relwidth=1, relheight=1) 

headling_label = Label(main_frame, text="Registration Form", fg="light Blue",
                       font=("times new roman", 32, "bold"), bg="black")
headling_label.grid(column=0, row=0, columnspan=2, pady=10)

name_label = Label(main_frame, text="Name", fg="white",
                   font=("Times new roman", 22, "bold"), bg="black")
name_label.grid(row=1, column=0, padx=20, pady=10)

name = StringVar()
name_entry = Entry(main_frame, textvariable=name, font=("times new roman", 18), bd=2, relief="groove")
name_entry.grid(column=1, row=1)

email_label = Label(main_frame, text="Email", fg="white",
                    font=("Times new roman", 22, "bold"), bg="black")
email_label.grid(row=2, column=0, padx=20, pady=10)

email = StringVar()
email_entry = Entry(main_frame, textvariable=email, font=("times new roman", 18), bd=2, relief="groove")
email_entry.grid(column=1, row=2)

phone_label = Label(main_frame, text="Phone", fg="white",
                    font=("Times new roman", 22, "bold"), bg="black")
phone_label.grid(row=3, column=0, padx=20, pady=10)

phone = StringVar()
phone_entry = Entry(main_frame, textvariable=phone, font=("times new roman", 18), bd=2, relief="groove")
phone_entry.grid(column=1, row=3)

password_label = Label(main_frame, text="Password", fg="white",
                       font=("Times new roman", 22, "bold"), bg="black")
password_label.grid(row=4, column=0, padx=20, pady=10)

password = StringVar()
password_entry = Entry(main_frame, textvariable=password, font=("times new roman", 18),
                       bd=2, relief="groove", show="*")
password_entry.grid(column=1, row=4)

confirm_password_label = Label(main_frame, text="Confirm Password", fg="white",
                               font=("Times new roman", 22, "bold"), bg="black")
confirm_password_label.grid(row=5, column=0, padx=20, pady=10)

confirm_password = StringVar()
confirm_password_entry = Entry(main_frame, textvariable=confirm_password, font=("times new roman", 18),
                               bd=2, relief="groove", show="*")
confirm_password_entry.grid(column=1, row=5)

result_label = Label(main_frame, bg="black", font=("times new roman", 16, "bold"))
result_label.grid(column=0, row=7, columnspan=2, pady=20)

def register():
    result_label.config(
        text=f"Name: {name.get()}\nEmail: {email.get()}\nPhone: {phone.get()}\nPassword: {password.get()}",
        fg="white"
    )

def delete_data():
    name.set("")
    email.set("")
    phone.set("")
    password.set("")
    confirm_password.set("")
    result_label.config(text="")

button_register = Button(main_frame, text="Register ✅", fg="green",bg="black",
                         font=("times new roman", 22, "bold"), command=register)
button_register.grid(column=1, row=6, pady=10)

button_delete = Button(main_frame, text="Delete ❌", fg="red",bg="black",
                       font=("times new roman", 22, "bold"), command=delete_data)
button_delete.grid(column=0, row=6, pady=10)

root.mainloop()
