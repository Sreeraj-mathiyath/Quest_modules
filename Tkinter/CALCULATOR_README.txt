README.txt
==================================================

        Simple Tkinter Calculator
        =========================

A beautiful and functional calculator built using Python's tkinter library.

Features:
---------
- Clean black & white modern design
- Custom window icon
- Fixed window size (non-resizable)
- Supports basic operations: +, -, ×, ÷, %
- Additional features:
    • Square (x²)
    • Double zero (00)
    • Decimal point (.)
    • Clear button (C)
- Error handling (division by zero, invalid input)
- Real-time input display with large readable font

Requirements:
-------------
- Python 3.x
- tkinter (included with standard Python)
- Icon image file: calculator.png
  Current path: D:\Quest\Tkinter\calculator.png

How to Run:
-----------
1. Save the code as calculator.py
2. Place the icon image "calculator.png" in the correct path OR
   Put it in the same folder and change this line:
   
   img = PhotoImage(file="calculator.png")

3. Run the program:
   python calculator.py

Button Functions:
-----------------
- 0-9, 00, .   → Enter numbers and decimals
- +, −, ×, ÷, % → Perform arithmetic operations
- x²           → Square the current number
- C            → Clear the display
- =            → Calculate and show result

Error Handling:
---------------
- Displays "Error" for:
    • Division by zero
    • Invalid expressions
    • Non-numeric input in operations

Design Highlights:
------------------
- Professional look with groove borders
- Highlight effect on entry field
- Large, easy-to-read buttons and text
- Blue highlight on "=" button when pressed

Future Improvements (Optional):
-------------------------------
- Add keyboard support
- Scientific functions (sin, cos, log, etc.)
- History panel
- Copy result to clipboard
- Theme switcher (dark/light)

==================================================
Thank you for using this calculator!
Feel free to modify and enhance it.

Made with Python + tkinter
==================================================