# from tkinter import *

# root = Tk()
# # #=========================window methods=========================================


# # root.title("My App")
# # icon  = PhotoImage(file=r"D:\Quest\Tkinter\google.png")
# # root.iconphoto(True,icon)
# # root.geometry("800x500+100+50")
# # # root.resizable(False,True)
# # root.maxsize(1000,800)
# # # root.state("zoomed")
# # root.attributes("-alpha",0.99)
# # root.attributes("-topmost",True)
# # # root.attributes("-transparentcolor","light blue")
# # # root.lift()
# # # root.lower()
# # root.config(bg="light blue",cursor="hand2",highlightcolor="white",highlightthickness=10)


# # #========================label====================================================
# # #used to display text or images on the window. It is non-interactive

# # l1 = Label(root,text="Hello Tkinter")
# # l1.pack()

# # #Text + Styling Example
# # l2 = Label(root,
# #            text="Python's Graphical User Interface📔",
# #            font=("Helvetica",20,"bold","italic"),
# #            fg="orange",
# #            bg="white",
# #            padx=20,
# #            pady=20
# #            )
# # l2.pack()

# # #Display Image in Label
# # img = PhotoImage(file=r"D:\Quest\Tkinter\google.png")
# # l3 = Label(root,
# #            image=img,
# #            background="white"
# #            )
# # l3.pack()

# # #Text + Image Together
# # l4 = Label(root,
# #            text="Text with image",
# #            font=("Algerian",18,"bold"),
# #            image=img,
# #            compound="bottom",
# #            background="white")
# # l4.pack()

# # #Changing Label Text Dynamically
# # l5 = Label(root,
# #            text="Original text",
# #            font=("arial",20))
# # l5.pack()

# # def update():
# #     l5.config(text="Text updated")

# # root.after(2000,update)

# # #Bind Mouse Events to Label (Advanced)


# # l6 = Label(root,text="Mouse event")
# # def on_enter(event):
# #     l6.config(bg="yellow")

# # def on_leave(event):
# #     l6.config(bg="blue")

# # l6.bind("<Enter>",on_enter)
# # l6.bind("<Leave>",on_leave)
# # l6.pack()


# # root.mainloop()


# #=================================Entry===================================
# # root1 = Tk()
# # root1.title("My App")
# # icon  = PhotoImage(file=r"D:\Quest\Tkinter\google.png")
# # root1.iconphoto(True,icon)
# # root1.geometry("800x500+100+50")
# # root1.maxsize(1000,800)
# # root1.attributes("-alpha",0.99)
# # root1.attributes("-topmost",True)
# # root1.config(bg="light blue",cursor="hand2",highlightcolor="white",highlightthickness=10)



# # data =StringVar()
# # e = Entry(root1,
# #           fg="orange",
# #           bg="white",
# #           font=("times new roman",20,"bold"),
# #           width=30,
# #           justify="center",
# #           textvariable=data,relief="sunken")
# # e.pack(padx=30,pady=30)
# # data.set("Welcome")
# # print(data.get())

# # # def show_value():
# # #     value = e.get()
# # #     e.insert(0,"hello")
# # #     print(value)

# # # button = Button(root1,command=show_value,text="show value")
# # # button.pack()



# # root1.mainloop()


# #=================================button======================================

# # def greet():
# #     print("Welcome!")

# # def process():
# #     btn3.config(text="Processing..........")

# # btn = Button(root, text="Disabled", state="disabled")
# # btn2 = Button(root, text="Enabled", state="normal")
# # btn3 = Button(root, text="Read Only", state="active",command=process)
# # btn.pack()
# # btn2.pack()
# # btn3.pack()
# # Button(root, text="Submit", bg="green", fg="white",
# #        font=("Arial", 14, "bold"), padx=10, pady=5).pack()

# # photo = PhotoImage(file="D:\Quest\Tkinter\google.png")
# # btn5 = Button(root, image=photo)
# # btn5.pack()

# # root.mainloop()


# #=============================text=======================================
# # t = Text(root, width=40, height=10, font=("Arial", 14), bg="lightyellow")
# # # t.pack()
# # scroll = Scrollbar(root)
# # scroll.pack(side=RIGHT, fill=Y)

# # t = Text(root, yscrollcommand=scroll.set)
# # t.pack()
# # scroll.config(command=t.yview)


# #-------------------select and replace ----------------------------------
# # t = Text(root, width=40, height=10)
# # t.pack()

# # entry = Entry(root, width=20)
# # entry.pack(pady=5)

# # def replace():
# #     try:
# #         new = entry.get()
# #         t.replace("sel.first", "sel.last", new)
# #     except:
# #         print("No selection!")

# # Button(root, text="Replace Selected Text", command=replace).pack()

# #----------------------highlight------------------------------------
# # t = Text(root, width=45, height=10, font=("Arial", 14))
# # t.pack(pady=10)

# # # Insert sample text
# # t.insert(END, "Python is powerful and easy to learn.\nSelect any part and highlight it!")

# # def highlight_selection():
# #     try:
# #         start = t.index("sel.first")
# #         end = t.index("sel.last")
# #         t.tag_add("highlight", start, end)
# #     except:
# #         print("No text selected!")

# # # Configure tag styles
# # t.tag_config("highlight", foreground="white", background="red", font=("Arial", 14, "bold"))

# # btn = Button(root, text="Highlight Selection", command=highlight_selection)
# # btn.pack()


# #---------------------search---------------------------------------
# # start = "1.0"
# # word = "Python"
# # pos = t.search(word, start, END)
# # print("Found at:", pos)


# #------------------copy,paste,cut,undo/redo------------------------




# root.mainloop()

# from tkinter import *

# root = Tk()
# root.title("Menubutton Example")

# mb = Menubutton(root, text="Options", relief="raised")
# mb.pack(pady=20)

# menu = Menu(mb, tearoff=0)
# mb["menu"] = menu

# menu.add_command(label="Save")
# menu.add_command(label="Update")
# menu.add_command(label="Delete")

# root.mainloop()




# from tkinter import *

# root = Tk()
# root.title("Menu Example")

# menubar = Menu(root)
# root.config(menu=menubar)

# file_menu = Menu(menubar, tearoff=0)
# menubar.add_cascade(label="File", menu=file_menu)
# file_menu.add_command(label="New")
# file_menu.add_command(label="Open")
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)

# root.mainloop()




