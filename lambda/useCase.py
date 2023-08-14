import tkinter as tk

window = tk.Tk()
window.geometry("200x200")
frame = tk.Frame(window)
frame.pack()

# def say_hi():
#     print("HELLO !") 

btn = tk.Button(frame, text="Click Me ", command=lambda : print("hello !!!!"))
btn.pack()

window.mainloop()