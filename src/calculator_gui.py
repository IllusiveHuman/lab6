import tkinter as tk
from tkinter import messagebox

def calculate(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Ошибка"

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":  # УБРАЛ ЛИШНЮЮ ЗАКРЫВАЮЩУЮ СКОБКУ
        entry_var.set(calculate(entry_var.get()))
    else:
        entry_var.set(entry_var.get() + button_text)

# Создание главного окна
root = tk.Tk()
root.title("Калькулятор")
root.geometry("300x400")

# Поле ввода
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right')
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, padx=10, pady=10)

# Кнопки калькулятора
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        button = tk.Button(root, text=text, font=("Arial", 20), width=5, height=2,
                           command=lambda t=text: on_click(t))
        button.grid(row=i+1, column=j, padx=5, pady=5)

if __name__ == "__main__":
    root.mainloop()
