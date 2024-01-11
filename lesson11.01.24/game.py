import tkinter




win = tkinter.Tk()

label = tkinter.Label(win, text='INGINIRIUM')
label.pack()

canvas = tkinter.Canvas(win, bg='white', width=400, height=400)

for i in range(1, 8, 1):
    canvas.create_line((50 * i, 0), (50 * i, 400), fill='black')
    canvas.create_line((0, 50 * i), (400, 50 * i), fill='black')

canvas.create_oval((300, 300), (350, 350), fill='yellow')
canvas.create_oval((0, 0), (50, 50), fill='yellow')
canvas.create_oval((50, 50), (100, 100), fill='yellow')
canvas.create_oval((100, 100), (150, 150), fill='yellow')
canvas.create_oval((150, 150), (100, 100), fill='yellow')
canvas.create_oval((300, 300), (350, 350), fill='yellow')
canvas.create_oval((300, 300), (350, 350), fill='yellow')
canvas.create_oval((300, 300), (350, 350), fill='yellow')
canvas.create_oval((300, 300), (350, 350), fill='yellow')
canvas.create_oval((300, 300), (350, 350), fill='yellow')
canvas.create_oval((300, 300), (350, 350), fill='yellow')
canvas.create_oval((300, 300), (350, 350), fill='yellow')













































canvas.pack()

win.mainloop()