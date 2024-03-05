import customtkinter
import tkinter.ttk
import tkinter.messagebox
import time

root = tkinter.Tk()
w = root.winfo_screenwidth() / 2 - 350
h = root.winfo_screenheight() / 2 - 250
root.geometry(f'700x500+{int(w)}+{int(h)}')
root.title('x=140 y=480')
root.resizable(width=False, height=False)
root['bg'] = 'grey40'

def mainFunc(btnName):
    if btnName == 'Головна':
        lastAction = customtkinter.CTkLabel(root, text='Ваші останні дії', font=('arial black', 24), text_color='grey90')
        lastAction.place(x = 315, y = 5)

    elif btnName == 'Вихід':
        askYN = tkinter.messagebox.askyesno(title='Вихід з програми', message='Ви дійсно бажаєте вийти?')
        if askYN == True:
            time.sleep(0.5)
            root.destroy()
        else:
            root.mainloop()

startProgText = customtkinter.CTkLabel(root, text='Моя бібліотека', text_color='grey80', font=('arial black', 34))
startProgText.place(x = 280, y = 140)
startProgText1 = customtkinter.CTkLabel(root, text='Програма з можливостями додавання та видаляння\n'
                                                   'книг, ')
startProgText1.place(x = 290, y = 250)
lst = ['Головна', 'Додати книги','Видалити книги', 'Моя бібліотека', 'Оцінити книги', 'Рейтинг книг', 'Історія', 'Очистити', 'Вихід']
frm1 = customtkinter.CTkFrame(root, width=140, height=510, fg_color='grey13')
frm1.place(x = 0, y = -3)
yIter = 20
for i in lst:
    btnFrame = customtkinter.CTkButton(frm1, text=f'{i}', height=37, hover_color='medium sea green', fg_color='grey24',
                                   corner_radius=6, width=126, font=('arial narrow', 15), command=lambda btnName=i: mainFunc(btnName))
    if i == 'Головна':
        btnFrame.place(x=7, y=yIter)
    elif i == 'Вихід':
        btnFrame.place(x=7, y=460)
    else:
        yIter += 42
        btnFrame.place(x = 7, y = yIter)

root.mainloop()