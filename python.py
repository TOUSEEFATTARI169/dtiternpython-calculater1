import tkinter as tk

root = tk.Tk()
root.title("DT Intern Calculator")


displayScreen = tk.Entry(root, width=22, borderwidth=5, bg="#282828", fg="white", font=("Helvetica", 20, "bold"), justify='right')
displayScreen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(number):
    current = displayScreen.get()
    displayScreen.delete(0, tk.END)
    displayScreen.insert(0, current + str(number))

def button_clear():
    displayScreen.delete(0, tk.END)

def button_equal():
    try:
        result = eval(displayScreen.get())
        displayScreen.delete(0, tk.END)
        displayScreen.insert(0, result)
    except:
        displayScreen.delete(0, tk.END)
        displayScreen.insert(0, "Error")

def button_decimal():
    current = displayScreen.get()
    if '.' not in current:
        displayScreen.insert(tk.END, '.')


button_font = ("Helvetica", 18, "bold")
button_color = "#ff5722" 
button_text_color = "white"
special_button_color = "#009688" 

# Number Buttons
buttons = [
    tk.Button(root, text=str(i), padx=20, pady=20, command=lambda i=i: button_click(i), bg=button_color, fg=button_text_color, font=button_font)
    for i in range(10)
]

# Special Function Buttons
button_add = tk.Button(root, text="+", padx=20, pady=20, command=lambda: button_click("+"), bg=special_button_color, fg=button_text_color, font=button_font)
button_subtract = tk.Button(root, text="-", padx=20, pady=20, command=lambda: button_click("-"), bg=special_button_color, fg=button_text_color, font=button_font)
button_multiply = tk.Button(root, text="*", padx=20, pady=20, command=lambda: button_click("*"), bg=special_button_color, fg=button_text_color, font=button_font)
button_divide = tk.Button(root, text="/", padx=20, pady=20, command=lambda: button_click("/"), bg=special_button_color, fg=button_text_color, font=button_font)
button_equal = tk.Button(root, text="=", padx=20, pady=20, command=button_equal, bg="#4caf50", fg=button_text_color, font=button_font)
button_clear = tk.Button(root, text="C", padx=20, pady=20, command=button_clear, bg="#f44336", fg=button_text_color, font=button_font)
button_decimal = tk.Button(root, text=".", padx=20, pady=20, command=button_decimal, bg=button_color, fg=button_text_color, font=button_font)

# Button Placement
buttons[1].grid(row=3, column=0, padx=5, pady=5)
buttons[2].grid(row=3, column=1, padx=5, pady=5)
buttons[3].grid(row=3, column=2, padx=5, pady=5)
buttons[4].grid(row=2, column=0, padx=5, pady=5)
buttons[5].grid(row=2, column=1, padx=5, pady=5)
buttons[6].grid(row=2, column=2, padx=5, pady=5)
buttons[7].grid(row=1, column=0, padx=5, pady=5)
buttons[8].grid(row=1, column=1, padx=5, pady=5)
buttons[9].grid(row=1, column=2, padx=5, pady=5)
buttons[0].grid(row=4, column=1, padx=5, pady=5)

button_add.grid(row=1, column=3, padx=5, pady=5)
button_subtract.grid(row=2, column=3, padx=5, pady=5)
button_multiply.grid(row=3, column=3, padx=5, pady=5)
button_divide.grid(row=4, column=3, padx=5, pady=5)

button_equal.grid(row=4, column=2, padx=5, pady=5)
button_clear.grid(row=4, column=0, padx=5, pady=5)
button_decimal.grid(row=4, column=1, padx=5, pady=5)

# Run loop
root.mainloop()
