from tkinter import *

root = Tk()
root.title("Calculator")
img = PhotoImage(file=r"D:\Quest\Tkinter\calculator.png")
root.iconphoto(True,img)
root.geometry("300x400")
root.resizable(False, False)
root.config(bg="black")


e1 = Entry(root, font=("times new roman",20), fg="black",bg="#FFFFFF", bd=2, relief="groove", 
           justify="right",highlightthickness=3,highlightbackground="#504444",highlightcolor="white",)
e1.grid(column=0, row=0, columnspan=4, padx=5, pady=5)

first_number = None
operator = None

def btn_click(val):
    e1.insert(END, val)

def btn_clear():
    e1.delete(0, END)

def set_operator(op):
    global first_number, operator

    if op == 'x²':
        try:
            num = float(e1.get())
            e1.delete(0, END)
            e1.insert(END, num ** 2)
        except:
            e1.delete(0, END)
            e1.insert(END, "Error")
        return
    
    first_number = float(e1.get())
    operator = op
    e1.insert(END, op)

def btn_equal():
    global first_number, operator
    try:
        expression = e1.get()
        
        second_num = float(expression.split(operator)[1])

        if operator == "+":
            result = first_number + second_num
        elif operator == "-":
            result = first_number - second_num
        elif operator == "*":
            result = first_number * second_num
        elif operator == "/":
            if second_num == 0:
                e1.delete(0, END)
                e1.insert(END, "Error")
                return
            result = first_number / second_num
        elif operator == "%":
            result = first_number % second_num

        e1.delete(0, END)
        e1.insert(END, result)

    except:
        e1.delete(0, END)
        e1.insert(END, "Error")


buttons = [
    ('%', 1, 0), ('x²', 1, 1), ('C', 1, 2), ('=', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3),
    ('0', 5, 0), ('00', 5, 1), ('.', 5, 2), ('/', 5, 3),
]

for (text, row, col) in buttons:
    if text == "C":
        Button(root, text=text, width=5, height=2, font=("times new roman",15),
               command=btn_clear).grid(row=row, column=col,padx=5,pady=5)
    elif text in "+-*/x²%":
        Button(root, text=text, width=5, height=2, font=("times new roman",15),
               command=lambda t=text: set_operator(t)).grid(row=row, column=col)
    elif text == "=":
        Button(root, text=text, width=5, height=2, font=("times new roman",15),activebackground="#4CC2FF",
               command=btn_equal).grid(row=row, column=col,padx=5,pady=5)
    else:
        Button(root, text=text, width=5, height=2, font=("times new roman",15),
               command=lambda t=text: btn_click(t)).grid(row=row, column=col,padx=5,pady=5)
        


root.mainloop()
