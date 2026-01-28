# # # from tkinter import *

# # # # # t = Tk()

# # # # # def anotherwindow():
# # # # #     top=Toplevel()
# # # # #     top.title("This is a Toplevel window")
# # # # #     top.geometry("200x200")
# # # # #     lbl=Label(top,text="Hello World")
# # # # #     lbl.pack()

# # # # # t.geometry("400x400")
# # # # # t.title("Main Window")
# # # # # btn = Button(t,text="Open a new window",command=anotherwindow)
# # # # # btn.pack()

# # # # # t.mainloop()

# # # root = Tk()
# # # root.title("Main Window")
# # # # root.geometry("400x400")
# # # # root.resizable(True,False)
# # # # root.maxsize(800,600)
# # # # root.minsize(200,200)
# # # root.iconphoto(True,PhotoImage(file=r"D:\Quest\Tkinter\google.png"))
# # # root.configure(background="light blue")
# # # # root.state('zoomed')
# # # # root.state('normal')
# # # # root.state('iconic')

# # # # root.attributes('-alpha',0.9)
# # # root.attributes('-topmost',True)
# # # root.attributes('-fullscreen',False)
# # # root.attributes('-disabled',False)
# # # root.attributes('-toolwindow',False)
# # # # root.attributes('-transparentcolor','red')
# # # root.mainloop()

# # # # import tkinter as tk

# # # # # root = tk.Tk()

# # # # # root.attributes("-alpha", 0.9)            # slight transparency
# # # # # root.attributes("-topmost", True)         # always on top
# # # # # root.attributes("-fullscreen", False)     # normal mode
# # # # # root.attributes("-toolwindow", True)      # small title bar (Windows)
# # # # # root.attributes("-transparentcolor", "white")  # make white fully transparent

# # # # root.mainloop()

# # import tkinter as tk
# # from tkinter import ttk

# # root = tk.Tk()
# # root.geometry("400x300")

# # ttk.Label(root, text="Name:").pack(pady=5)
# # ttk.Entry(root).pack(pady=5)

# # ttk.Button(root, text="Submit").pack(pady=5)

# # ttk.Combobox(root, values=["Python", "Java", "C++"]).pack(pady=5)

# # ttk.Progressbar(root,value=50 ,length=150, mode='determinate').pack(pady=5)

# # root.mainloop()



# from tkinter import *

# #----------------------Label--------------------------------------
# # root=Tk()
# # root.title("Label")
# # root.config(background="light blue")
# # label=Label(root,text="Hello Tkinter",font=("Arial",22),fg="blue")
# # label.pack()

# # img=PhotoImage(r"D:\Quest\Tkinter\google.png")

# # l2=Label(root,text="Label testing",font=("Times New Roamn",40),fg="pink",bg="white")
# # l2.pack()
# # root.mainloop()

# # a1 =Tk()
# # l1=Label(a1,text="Enter Your Name:")
# # l1.pack()
# # l2=Entry(a1,width=20)
# # l2.pack()

# # a1.mainloop()


# #------------------Entry-------------------------------

# # root =Tk()
# # name_var = StringVar()

# # e1 = Entry(root,textvariable=name_var,width=25,font=("Arial",16),fg="red",bg="light blue",show="*")
# # e1.pack(pady=10)

# # def show():
# #     print("Stored value:", name_var.get())
# #     label_result.config(text=f"you types : {name_var.get()}")

# # button = Button(root,text="show value",command=show)
# # button.pack(pady=10)

# # label_result=Label(root,font=("Arial",14))
# # label_result.pack(pady=10)
# # root.mainloop()

# #-----------------------Button--------------------------------
# # from tkinter import ttk

# # root = Tk()

# # button = Button(root,text="click")
# # button.pack(pady=10)

# # b1 = ttk.Button(root,text="themed button")
# # b1.pack(pady=10)

# # def on_enter(e):
# #     b2.config(bg="green", fg="white")

# # def on_leave(e):
# #     b2.config(bg="lightgray", fg="black")

# # b2 = Button(root, text="Hover Me", bg="lightgray")
# # b2.pack(pady=10)

# # b2.bind("<Enter>", on_enter)
# # b2.bind("<Leave>", on_leave)

# # style = ttk.Style()
# # style.configure("TButton", padding=6)
# # style.map("TButton",
# #           background=[("active", "#4CAF50")],
# #           foreground=[("active", "white")])

# # btn = ttk.Button(root, text="Hover Stylish Button", style="TButton")
# # btn.pack(pady=10)

# # root.mainloop()


# # import tkinter as tk
# # import threading
# # import time

# # root = tk.Tk()
# # root.title("Button Loading Animation")

# # loading = False   # global flag

# # def long_task():
# #     """Simulated long-running task"""
# #     time.sleep(5)   # 5 seconds task

# # def animate_loading():
# #     """Animate dots while task is running"""
# #     dots = ["", ".", "..", "..."]
# #     i = 0
# #     while loading:
# #         button.config(text=f"Loading{dots[i % 4]}")
# #         i += 1
# #         time.sleep(0.4)

# #     button.config(text="Start Task", state="normal")  # reset button after task

# # def run_process():
# #     global loading
# #     loading = True
# #     button.config(state="disabled")  # disable button during task

# #     threading.Thread(target=animate_loading, daemon=True).start()
# #     threading.Thread(target=background_job, daemon=True).start()

# # def background_job():
# #     global loading
# #     long_task()
# #     loading = False   # stop animation

# # button = tk.Button(root, text="Start Task", command=run_process, font=("Arial", 14))
# # button.pack(pady=20)

# # root.mainloop()


# # root = Tk()

# # root.geometry("400x300")

# # text = Text(root,height=10,width=10)
# # text.pack(pady=10)

# # text.insert("1.0","this is a test widget\n")
# # text.insert("end","you can write mutiple lines here")

# # def display():
# #     value = text.get("1.0","end")
# #     print(value)

# # def clear():
# #     text.delete("1.0","end")


# # b1 = Button(root,text="Print",command=display).pack(pady=10)
# # b2 = Button(root,text="Delete",command=clear).pack(pady=10)

# # root.mainloop()


# # root = Tk()
# # root.geometry("400x300")

# # text = Text(root, height=10, width=40)
# # text.pack()

# # def add_line():
# #     text.insert("end", "New line appended!\n")
# #     text.see("end")   # Auto-scroll to bottom
# #     text.focus()      # Keep cursor focused in the text box

# # Button(root, text="Add Line", command=add_line).pack(pady=5)

# # root.mainloop()


# # import tkinter as tk

# # root = tk.Tk()

# # text = tk.Text(root, height=8, width=40)
# # text.pack(padx=10, pady=10)

# # def show_cursor_pos(event=None):
# #     index = text.index("insert")   # Current cursor index
# #     print("Cursor at:", index)

# # text.bind("<KeyRelease>", show_cursor_pos)

# # root.mainloop()



# import tkinter as tk

# root = tk.Tk()
# root.geometry("400x300")

# text = tk.Text(root, undo=True)  # Enable undo system
# text.pack(expand=True, fill="both")

# def move_cursor():
#     text.mark_set("insert", "1.0")  # Move cursor to start

# def undo():
#     text.edit_undo()

# def redo():
#     text.edit_redo()

# tk.Button(root, text="Move Cursor to Beginning", command=move_cursor).pack()
# tk.Button(root, text="Undo", command=undo).pack()
# tk.Button(root, text="Redo", command=redo).pack()

# root.mainloop()




# import tkinter as tk

# root = tk.Tk()
# root.geometry("400x300")

# frame = tk.Frame(root, bg="lightgray", padx=10, pady=10)
# frame.pack(pady=20)

# tk.Label(frame, text="Username").pack()
# tk.Entry(frame).pack()
# tk.Button(frame, text="Login").pack()

# root.mainloop()



# import tkinter as tk

# root = tk.Tk()
# root.geometry("350x200")

# var = tk.IntVar()

# check = tk.Checkbutton(
#     root,
#     text="Enable Notifications",
#     variable=var,
#     onvalue=1,
#     offvalue=0,
#     font=("Arial", 12),
#     bg="lightyellow",
#     fg="blue",
#     selectcolor="orange",
#     activebackground="yellow",
#     padx=10,
#     pady=5
# )
# check.pack(pady=20)

# root.mainloop()



# import tkinter as tk

# root = tk.Tk()
# root.geometry("300x250")

# info_frame = tk.LabelFrame(root, text="User Info", padx=10, pady=10)
# info_frame.pack(padx=20, pady=20)

# tk.Label(info_frame, text="Name:").grid(row=0, column=0, sticky="w")
# tk.Entry(info_frame).grid(row=0, column=1)

# tk.Label(info_frame, text="Email:").grid(row=1, column=0, sticky="w")
# tk.Entry(info_frame).grid(row=1, column=1)

# root.mainloop()



# import tkinter as tk

# root = tk.Tk()
# root.geometry("250x200")

# lb = tk.Listbox(root,selectmode="multiple",activestyle="dotbox")
# lb.pack(pady=10)

# lb.insert(0, "Python")
# lb.insert(1, "Java")
# lb.insert(2, "C++")
# lb.insert(3, "JavaScript")
# lb.insert(4, "Python")
# lb.insert(5, "Java")
# lb.insert(6, "C++")
# lb.insert(7, "JavaScript")
# lb.insert(0, "Python")
# lb.insert(1, "Java")
# lb.insert(2, "C++")
# lb.insert(3, "JavaScript")
# lb.insert(0, "Python")
# lb.insert(1, "Java")
# lb.insert(2, "C++")
# lb.insert(3, "JavaScript")
# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# root.title("Scrollbar Example")

# listbox = tk.Listbox(root, height=10, width=30)
# listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# scroll = tk.Scrollbar(root, orient=tk.VERTICAL, command=listbox.yview)
# scroll.pack(side=tk.RIGHT, fill=tk.Y)

# listbox.config(yscrollcommand=scroll.set)

# for i in range(1, 101):
#     listbox.insert(tk.END, f"Item {i}")

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# root.title("Scrollbar .set() Example")

# # Create a Text widget
# text = tk.Text(root, height=10, width=40, wrap="none")
# text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# # Create a Scrollbar
# scroll = tk.Scrollbar(root, orient=tk.VERTICAL)
# scroll.pack(side=tk.RIGHT, fill=tk.Y)

# # Connect Text -> Scrollbar and Scrollbar -> Text
# text.config(yscrollcommand=scroll.set)
# scroll.config(command=text.yview)

# # Insert many lines to show scrolling
# for i in range(1, 101):
#     text.insert(tk.END, f"Line {i}\n")


# # 🔹 MANUAL DEMO OF scroll.set(first, last)
# # Button to set the scrollbar halfway manually
# def set_half_scroll():
#     scroll.set(0.5, 0.6)   # scrollbar thumb from 50% to 60%

# btn = tk.Button(root, text="Move scrollbar to middle", command=set_half_scroll)
# btn.pack()

# root.mainloop()


# import tkinter as tk

# root = tk.Tk()
# root.title("Canvas Example")

# canvas = tk.Canvas(root, width=400, height=300, bg="white")
# canvas.pack()

# # Draw shapes
# canvas.create_line(50, 50, 200, 50, fill="blue", width=3)
# canvas.create_rectangle(50, 100, 200, 200, outline="green", width=3)
# canvas.create_oval(250, 100, 350, 200, fill="yellow")
# canvas.create_text(200, 250, text="Hello Canvas", font=("Arial", 16), fill="purple")

# root.mainloop()



# from tkinter import *

# root = Tk()

# mb = Menubutton(root, text="Settings")
# mb.pack(pady=10)

# main_menu = Menu(mb, tearoff=0)
# mb.config(menu=main_menu)

# main_menu.add_command(label="Profile")
# main_menu.add_command(label="Security")

# # Submenu
# theme_menu = Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="Theme", menu=theme_menu)
# theme_menu.add_command(label="Light")
# theme_menu.add_command(label="Dark")

# root.mainloop()


# from tkinter import *

# root = Tk()

# msg = Message(root,
#               text="This is a long message that will automatically wrap when it reaches the specified width.",
#               width=200)
# msg.pack(pady=10)

# root.mainloop()




# from tkinter import *

# root = Tk()

# def on_select(*args):
#     print("Selected:", var.get())

# var = StringVar()
# var.set("Male")
# var.trace("w", on_select)

# opt = OptionMenu(root, var, "Male", "Female", "Other")
# opt.pack(pady=10)

# root.mainloop()


# from tkinter import *
# from tkinter.ttk import Combobox

# root = Tk()

# def show():
#     print("Selected:", cb.get())

# cb = Combobox(root, values=["Python", "Java", "C++"])
# cb.current(0)   # default selection
# cb.pack(pady=10)

# Button(root, text="Print Value", command=show).pack()

# root.mainloop()

# from tkinter import *
# from tkinter.ttk import Treeview

# root = Tk()

# tree = Treeview(root, columns=("age", "city"), show="headings")
# tree.pack()

# tree.heading("age", text="Age")
# tree.heading("city", text="City")

# tree.insert("", "end", values=(25, "Mumbai"))
# tree.insert("", "end", values=(30, "Delhi"))

# root.mainloop()



# from tkinter import *
# from tkinter.ttk import Progressbar

# root = Tk()
# root.title("Determinate Progressbar")

# pb = Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
# pb.pack(pady=20)

# def run():
#     pb["maximum"] = 100
#     for i in range(101):
#         pb["value"] = i
#         root.update()   # refresh UI
#         root.after(50)  # delay for demo

# Button(root, text="Start", command=run).pack()
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import Progressbar

# root = Tk()
# root.title("Indeterminate Progressbar")

# pb = Progressbar(root, orient=HORIZONTAL, length=300, mode='indeterminate')
# pb.pack(pady=20)

# def start():
#     pb.start(10)   # speed of animation (ms)

# def stop():
#     pb.stop()

# Button(root, text="Start", command=start).pack()
# Button(root, text="Stop", command=stop).pack()

# root.mainloop()



# from tkinter import *

# root = Tk()
# label = Label(root, text="Events Demo", font=("Arial", 18), bg="lightblue")
# label.pack(padx=30, pady=30)

# def info(event):
#     print("Event →", event.type, "|", "Key/Mouse →", event.keysym if hasattr(event, 'keysym') else event.num)

# label.bind("<Enter>", info)
# label.bind("<Leave>", info)
# label.bind("<Button-1>", info)
# label.bind("<Double-Button-1>", info)
# label.bind("<Motion>", info)
# root.bind("<Key>", info)

# root.mainloop()


from tkinter import *

root = Tk()
root.geometry("300x200")

def toggle():
    if password.cget("show") == "":
        password.config(show="*")
        btn.config(text="Show")
    else:
        password.config(show="")
        btn.config(text="Hide")

Label(root, text="Username").pack()
username = Entry(root)
username.pack()

Label(root, text="Password").pack()
password = Entry(root, show="*")
password.pack()

btn = Button(root, text="Show", command=toggle)
btn.pack()

def login(event=None):
    print("Username:", username.get())
    print("Password:", password.get())

password.bind("<Return>", login)  # Enter to login
Button(root, text="Login", command=login).pack()

root.mainloop()
