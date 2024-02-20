import tkinter
import datetime

root = tkinter.Tk()
w = root.winfo_screenwidth() / 2 - 250
h = root.winfo_screenheight() / 2 - 250
root.geometry(f'500x500+{int(w)}+{int(h)}')
root.wm_resizable(width=False,height=False)
root.title('Clicker')
def result():
    root1 = tkinter.Tk()
    w1 = root1.winfo_screenwidth() / 2 - 125
    h1 = root1.winfo_screenheight() / 2 - 75
    root1.geometry(f'250x150+{int(w1)}+{int(h1)}')
    root1.wm_resizable(width=False, height=False)
    tkinter.Label(root1, text='Hello').pack()
x = 0
clicks = 0
clicksVisual = (tkinter.Label(root, text=f'{clicks}'))
clicksVisual.pack()
def clicker():
    global btn, x, clicks
    clicks += 1
    clicksVisual.config(text=f'{clicks}')
def ttime():
    dt = datetime.time(0,0,10)
    tkinter.Label(root, text=f'{dt}').pack()
btn = tkinter.Button(root, text='Click', command=clicker).pack()
ttime()
root.mainloop()