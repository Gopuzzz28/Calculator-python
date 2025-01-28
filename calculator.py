import tkinter as tk

def press(key):
    entry_text.set(entry_text.get() + str(key))

def evaluate():
    try:
        result = eval(entry_text.get())
        entry_text.set(result)
    except:
        entry_text.set("Error")

def clear():
    entry_text.set("")

root = tk.Tk()
root.title("Modern Calculator")

root.geometry("400x600")
root.config(bg="#2C3E50")

entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 24), bd=10, relief="sunken", justify="right", bg="#34495E", fg="white")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 18), bg="#E67E22", fg="white", command=evaluate)
    elif text == "C":
        btn = tk.Button(root, text=text, font=("Arial", 18), bg="#E74C3C", fg="white", command=clear)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18), bg="#34495E", fg="white", command=lambda t=text: press(t))
    
    btn.grid(row=row, column=col, sticky="nsew", ipadx=20, ipady=20)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
