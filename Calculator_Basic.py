from tkinter import *
from colors import *
# creating main object
root = Tk()
# For validation
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'e']
operator_list = ['+', '-', '*', '**', '/', '//', '.', '(', ')']
calculation = False
screen_value = StringVar()
string_fill = "0"
screen_value.set(string_fill)


# Function for validation
def get_value():
    string = ""
    values = screen.get()
    for value in values:
        if value in numbers_list or value in operator_list:
            string = string + value
    if values == '0':
        string = ""
    return string


# Function to do calculation
def calculate():
    string = get_value()
    result = eval(string)
    screen_value.set(result)


# Function to enter number by button
def number_btn(num):
    string = get_value()
    string = string + num
    screen_value.set(string)


# Function to enter symbol by button
def operator_btn(operator):
    string = get_value()
    string = string + operator
    screen_value.set(string)


# Function to clear window by button
def clear_btn():
    screen_value.set("0")


# Function to get keypress
def key(event):
    # Get the keypress
    my_input = event.keycode
    string = get_value()  # get the existing value of screen
    kp = repr(event.char)
    if my_input == 9:
        # Exit when escape key is pressed
        root.destroy()
    elif my_input == 119 or my_input == 22:
        # Delete last later when del key or backspace key is pressed
        new = string[:-1]
        if len(string) == 1 or len(string) == 0:
            string = "0"
        else:
            string = new
    elif my_input == 36:
        # Calculate the result when enter key is pressed
        result = eval(string)
        string = str(result)
    if kp[1] in numbers_list or kp[1] in operator_list:
        num = kp[1]
    else:
        num = ''
    string = string + num
    screen_value.set(string)
    # To handle the bug
    string = get_value()
    if string == "":
        screen_value.set("0")


# Window behaviour
root.resizable(height=0, width=0)
root.title("Rudransh's Calculator")
root.configure(background=background)

# input output screen
screen = Entry(root,
               font=("cursive", 33, "bold"),
               background=display,
               state='disabled',
               cursor='arrow',
               disabledbackground=display,
               disabledforeground=text,
               fg=display_font,
               relief=SUNKEN,
               border=0,
               highlightcolor=background,
               textvariable=screen_value,
               justify="right"
               )

button1 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="MC",
                 background=button_top,
                 fg=text,
                 activebackground=button_top_active,
                 activeforeground=text,
                 padx=38,
                 pady=10
                 )

button2 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="M+",
                 background=button_top,
                 fg=text,
                 activebackground=button_top_active,
                 activeforeground=text,
                 padx=38,
                 pady=10
                 )

button3 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="÷",
                 background=symbol,
                 fg=symbol_font,
                 activebackground=symbol_active,
                 activeforeground=symbol_font,
                 padx=50,
                 pady=10,
                 command=lambda: operator_btn("/")
                 )

button4 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="×",
                 background=symbol,
                 fg=symbol_font,
                 activebackground=symbol_active,
                 activeforeground=symbol_font,
                 padx=50,
                 pady=10,
                 command=lambda: operator_btn("*")
                 )

button5 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="7",
                 background=button,
                 fg=text,
                 activebackground=button_active,
                 activeforeground=text,
                 padx=50,
                 pady=10,
                 command=lambda: number_btn("7")
                 )

button6 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="8",
                 background=button,
                 fg=text,
                 activebackground=button_active,
                 activeforeground=text,
                 padx=50,
                 pady=10,
                 command=lambda: number_btn("8")
                 )

button7 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="9",
                 background=button,
                 fg=text,
                 activebackground=button_active,
                 activeforeground=text,
                 padx=50,
                 pady=10,
                 command=lambda: number_btn("9")
                 )

button8 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="-",
                 background=symbol,
                 fg=symbol_font,
                 activebackground=symbol_active,
                 activeforeground=symbol_font,
                 padx=50,
                 pady=10,
                 command=lambda: operator_btn("-")
                 )

button9 = Button(root,
                 font=("cursive", 20, "bold"),
                 border=2,
                 relief=RAISED,
                 text="4",
                 background=button,
                 fg=text,
                 activebackground=button_active,
                 activeforeground=text,
                 padx=50,
                 pady=10,
                 command=lambda: number_btn("4")
                 )

button10 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="5",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=lambda: number_btn("5")
                  )

button11 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="6",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=lambda: number_btn("6")
                  )

button12 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="+",
                  background=symbol,
                  fg=symbol_font,
                  activebackground=symbol_active,
                  activeforeground=symbol_font,
                  padx=50,
                  pady=10,
                  command=lambda: operator_btn("+")
                  )

button13 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="1",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=lambda: number_btn("1")
                  )

button14 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="2",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=lambda: number_btn("2")
                  )

button15 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="3",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=lambda: number_btn("3")
                  )

button16 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="=",
                  background=equal,
                  fg=text,
                  activebackground=button_equal,
                  activeforeground=text,
                  padx=50,
                  pady=10,
                  command=calculate
                  )

button17 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="0",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=119,
                  pady=10,
                  command=lambda: number_btn("0")
                  )

button18 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text=".",
                  background=button,
                  fg=text,
                  activebackground=button_active,
                  activeforeground=text,
                  padx=52,
                  pady=10,
                  command=lambda: number_btn(".")
                  )

button19 = Button(root,
                  font=("cursive", 20, "bold"),
                  border=2,
                  relief=RAISED,
                  text="CLEAR",
                  background=clear,
                  fg=background,
                  activebackground=clear_active,
                  activeforeground=background,
                  padx=16,
                  pady=10,
                  command=clear_btn
                  )

# Styling
screen.config(highlightbackground=background, highlightthickness=5)
button1.config(highlightbackground=background, highlightthickness=5)
button2.config(highlightbackground=background, highlightthickness=5)
button3.config(highlightbackground=background, highlightthickness=5)
button4.config(highlightbackground=background, highlightthickness=5)
button5.config(highlightbackground=background, highlightthickness=5)
button6.config(highlightbackground=background, highlightthickness=5)
button7.config(highlightbackground=background, highlightthickness=5)
button8.config(highlightbackground=background, highlightthickness=5)
button9.config(highlightbackground=background, highlightthickness=5)
button10.config(highlightbackground=background, highlightthickness=5)
button11.config(highlightbackground=background, highlightthickness=5)
button12.config(highlightbackground=background, highlightthickness=5)
button13.config(highlightbackground=background, highlightthickness=5)
button14.config(highlightbackground=background, highlightthickness=5)
button15.config(highlightbackground=background, highlightthickness=5)
button16.config(highlightbackground=background, highlightthickness=5)
button17.config(highlightbackground=background, highlightthickness=5)
button18.config(highlightbackground=background, highlightthickness=5)
button19.config(highlightbackground=background, highlightthickness=5)

# First Row
screen.grid(columnspan=4)

# Second row
button1.grid(column=0, row=1)
button2.grid(column=1, row=1)
button3.grid(column=2, row=1)
button4.grid(column=3, row=1)

# Third Row
button5.grid(column=0, row=2)
button6.grid(column=1, row=2)
button7.grid(column=2, row=2)
button8.grid(column=3, row=2)

# Fourth Row
button9.grid(column=0, row=3)
button10.grid(column=1, row=3)
button11.grid(column=2, row=3)
button12.grid(column=3, row=3)

# Fifth Row
button13.grid(column=0, row=4)
button14.grid(column=1, row=4)
button15.grid(column=2, row=4)
button16.grid(column=3, row=4)

# Sixth Row
button17.grid(columnspan=2, column=0, row=5)
button18.grid(column=2, row=5)
button19.grid(column=3, row=5)

# Bind Keypress
root.bind("<Key>", key)
# Starting main gui window
root.mainloop()
