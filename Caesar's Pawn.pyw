from tkinter import *
from tkinter import messagebox
import webbrowser

window = Tk()
window.resizable(width=False, height=False)
window['bg'] = '#8B0000'
window.title("Caesar's Pawn v0.9")
# коммент со скрытым майнером
window.geometry('450x320+700+350')
window.iconbitmap('icon.ico')

message = StringVar()
key = StringVar()
state = BooleanVar()

Label(window,
      text="Caesar's Pawn",
      font='AdobeFangsongStd-Regular 30',
      fg='#FFD700',
      bg='#8B0000'
      ).place(x=0, y=0)

Label(window,
      text='Enter the key',
      font='AdobeFangsongStd-Regular',
      fg='#FFD700',
      bg='#8B0000'
      ).place(x=0, y=60)

Entry(window,
      width=28,
      textvariable=key,
      bg='#8B0000',
      fg='#FFD700',
      font='AdobeFangsongStd-Regular'
      ).place(x=150, y=65)

Label(window,
      text='Enter the message',
      fg='#FFD700',
      bg='#8B0000',
      font='AdobeFangsongStd-Regular'
      ).place(x=0, y=90)

Entry(window,
      width=28,
      textvariable=message,
      bg='#8B0000',
      fg='#FFD700',
      font='AdobeFangsongStd-Regular'
      ).place(x=150, y=95)


def answer():
    code = ''
    sign = -1
    if state.get():
        sign = 1
    if not message.get().isalpha():
        messagebox.showerror('Ошибочка...', 'Введите строку')
    try:
        for i in message.get():
            k = ord(i) + int(key.get()) * sign
            if k < 97:
                k += 26
            code += chr(k)
        text_box.delete('1.0', END)
        text_box.insert('1.0', code)
        window.title('Ave Caesar! Morituri te salutant')
    except ValueError:
        messagebox.showerror('Ошибочка...', 'Введите число')


Button(window,
       text='Confirm',
       command=answer,
       fg='#FFD700',
       bg='#8B0000',
       font='AdobeFangsongStd-Regular',
       activebackground='#8B0000',
       activeforeground='#FFD700',
       cursor="hand2"
       ).place(x=0, y=125)

Checkbutton(window,
            text='Reverse(beta)',
            var=state,
            fg='#FFD700',
            bg='#8B0000',
            font='AdobeFangsongStd-Regular',
            selectcolor='#8B0000',
            activebackground='#8B0000',
            activeforeground='#FFD700'
            ).place(x=80, y=125)

answ = Label(window,
             text="",
             fg='#FFD700',
             bg='#8B0000')
answ.grid(column=0, row=5, sticky=SW)

text_box = Text(
    width=50,
    height=6,
    fg='#FFD700',
    bg='#8B0000',
    font='AdobeFangsongStd-Regular')
text_box.place(x=0, y=170)


def open_author(event):
    webbrowser.open_new("https://www.youtube.com/watch?v=Nx-ZFAgIWzI")


link = Label(window,
             text="By TakPlintus",
             fg="#FFD700",
             font='AdobeFangsongStd-Regular',
             cursor="hand2",
             bg='#8B0000')
link.place(x=348, y=292)
link.bind('<Button-1>', open_author)

window.mainloop()
