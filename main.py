import tkinter as tk

root = tk.Tk()
root.title("The Calculator")
root.geometry("400x500")

# Title
headtitle = tk.Label(root, text="The Calculator", font="Verdana 14")
headtitle.pack(anchor='center', pady=20)

# Information text
info = tk.Label(root, text="1", font="Verdana 10")
info.pack(anchor='w', padx=20, pady=20)

# Buttons
buttons = tk.Frame(root, bg='red', width='500')
buttons.pack(side="left")
btn = tk.Button(buttons, text="hello")
btn.pack(side="left")


root.mainloop()
