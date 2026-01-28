from tkinter import *
from re import *

root = Tk()
back_ground = PhotoImage(file=r"D:\Quest\Tkinter\download (3).png")
root.title("registration Form")
root.geometry("800x500")
root.config(bg="white")

bg_label = Label(root, image=back_ground)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

main_frame = Frame(root, bg="black")
main_frame.place(relx=0.5, rely=0.5, anchor="center")

headling_label = Label(main_frame, text="Registration Form", fg="light blue",
                       font=("times new roman", 32, "bold"), bg="black")
headling_label.grid(column=0, row=0, columnspan=2, pady=10)

# ---------------- Variables ----------------
name = StringVar()
email = StringVar()
phone = StringVar()
password = StringVar()
confirm_password = StringVar()

# ---------------- Labels & Entry ----------------
Label(main_frame, text="Name", fg="white", font=("Times new roman", 22, "bold"), bg="black").grid(row=1, column=0, padx=20, pady=10)
Entry(main_frame, textvariable=name, font=("times new roman", 18), bd=2, relief="groove").grid(column=1, row=1)

Label(main_frame, text="Email", fg="white", font=("Times new roman", 22, "bold"), bg="black").grid(row=2, column=0, padx=20, pady=10)
Entry(main_frame, textvariable=email, font=("times new roman", 18), bd=2, relief="groove").grid(column=1, row=2)

Label(main_frame, text="Phone", fg="white", font=("Times new roman", 22, "bold"), bg="black").grid(row=3, column=0, padx=20, pady=10)
Entry(main_frame, textvariable=phone, font=("times new roman", 18), bd=2, relief="groove").grid(column=1, row=3)

Label(main_frame, text="Password", fg="white", font=("Times new roman", 22, "bold"), bg="black").grid(row=4, column=0, padx=20, pady=10)
Entry(main_frame, textvariable=password, font=("times new roman", 18), bd=2, relief="groove", show="*").grid(column=1, row=4)

Label(main_frame, text="Confirm Password", fg="white", font=("Times new roman", 22, "bold"), bg="black").grid(row=5, column=0, padx=20, pady=10)
Entry(main_frame, textvariable=confirm_password, font=("times new roman", 18),
      bd=2, relief="groove", show="*").grid(column=1, row=5)

result_label = Label(main_frame, bg="black", font=("times new roman", 16, "bold"))
result_label.grid(column=0, row=7, columnspan=2, pady=20)


# ---------------- Validation Function ----------------
def register():
    n = name.get().strip()
    e = email.get().strip()
    p = phone.get().strip()
    pw = password.get().strip()
    cpw = confirm_password.get().strip()

    # Name Validation
    if n == "":
        result_label.config(text="Name cannot be empty", fg="red")
        return
    if not match(r"^[A-Za-z ]+$", n):
        result_label.config(text="Name must contain only alphabets", fg="red")
        return
    if len(n) < 3:
        result_label.config(text="Name must be at least 3 characters long", fg="red")
        return

    # Email Validation
    if e == "":
        result_label.config(text="Email cannot be empty", fg="red")
        return
    if not match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", e):
        result_label.config(text="Invalid email format", fg="red")
        return

    # Phone Validation
    if p == "":
        result_label.config(text="Phone number cannot be empty", fg="red")
        return
    if not (p.isdigit() and len(p) == 10):
        result_label.config(text="Phone number must be 10 digits", fg="red")
        return

    # Password Validation
    if pw == "":
        result_label.config(text="Password cannot be empty", fg="red")
        return
    if len(pw) < 8:
        result_label.config(text="Password must be at least 8 characters", fg="red")
        return
    if pw != cpw:
        result_label.config(text="Password and Confirm Password do not match", fg="red")
        return

    result_label.config(text=f"✔ Registration Successful!\n\n"
                             f"Name: {n}\nEmail: {e}\nPhone: {p}",
                        fg="light green")


# ---------------- Clear Function ----------------
def delete_data():
    name.set("")
    email.set("")
    phone.set("")
    password.set("")
    confirm_password.set("")
    result_label.config(text="")


# ---------------- Buttons ----------------
Button(main_frame, text="Register ✅", fg="green", bg="black",
       font=("times new roman", 22, "bold"), command=register).grid(column=1, row=6, pady=10)

Button(main_frame, text="Delete ❌", fg="red", bg="black",
       font=("times new roman", 22, "bold"), command=delete_data).grid(column=0, row=6, pady=10)

root.mainloop()
