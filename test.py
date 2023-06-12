import tkinter as tk

master = tk.Tk()

def line(x1, y1, x2, y2):
    print(x1, y1, x2, y2)
    w.create_line(x1, y1, x2, y2, fill="green")


w = tk.Canvas(master, width=800, height=100)
w.pack()

l1 = w.create_text(50, 20, text="ONE", fill="red", tag="l1")
l2 = w.create_text(720, 20, text="TWO", fill="blue", tag="l2")
x1 = w.coords(l1)[0] + 20
y1 = w.coords(l1)[1]
x2 = w.coords(l2)[0] - 20
y2 = w.coords(l2)[1]
line(x1, y1, x2, y2)

master.mainloop()