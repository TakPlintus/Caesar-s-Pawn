from tkinter import *
from tkinter import messagebox
from webbrowser import open_new
from win32clipboard import GetClipboardData, OpenClipboard

window = Tk()
window.resizable(width=False, height=False)
window['bg'] = '#8B0000'
window.title("Caesar's Pawn v1.0")
# коммент со скрытым майнером
window.geometry('450x320+700+350')
window.iconbitmap('Data/icon.ico')

entry_text = StringVar()
entry_key = StringVar()
encrypt_state = BooleanVar()
eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

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
      textvariable=entry_key,
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
      textvariable=entry_text,
      bg='#8B0000',
      fg='#FFD700',
      font=('Times New Roman', 15)
      ).place(x=150, y=95)


def encrypt():
    key = 0
    try:
        key = abs(int(entry_key.get()))
    except ValueError:
        messagebox.showerror('Ошибочка...', 'Ключ должен быть числом!')
    text = entry_text.get()
    text2 = ''
    if encrypt_state.get():
        key = -key
    for i in range(len(text)):
        t = text[i].lower()
        if t in eng_alphabet:
            s = eng_alphabet.find(t)
            if s + abs(key) >= len(eng_alphabet):
                s = ((key + s) % len(eng_alphabet))
                text2 += eng_alphabet[s].upper() if text[i].isupper() else eng_alphabet[s]
            else:
                s += key
                text2 += eng_alphabet[s].upper() if text[i].isupper() else eng_alphabet[s]
        elif t in rus_alphabet:
            s = rus_alphabet.find(t)
            if s + abs(key) >= len(rus_alphabet):
                s = (key + s) % len(rus_alphabet)
                text2 += rus_alphabet[s].upper() if text[i].isupper() else rus_alphabet[s]
            else:
                s += key
                text2 += rus_alphabet[s].upper() if text[i].isupper() else rus_alphabet[s]
        else:
            text2 += text[i]
    text_box.delete('1.0', END)
    text_box.insert('1.0', text2)
    window.title('Ave Caesar! Morituri te salutant')


def encrypt_window():
    window2 = Toplevel()
    window2.geometry('600x750')
    window2.title('Deciphering the Caesar Cipher')
    window2.iconbitmap('Data/Icon.ico')
    window2['bg'] = 'black'

    frame_cnt = 5
    frames = [PhotoImage(file='Data/background.gif', format='gif -index %i' % i) for i in range(frame_cnt)]

    def update(ind):
        frame = frames[ind]
        ind += 1
        if ind == frame_cnt:
            ind = 0
        gif.configure(image=frame)
        window2.after(70, update, ind)

    gif = Label(window2, borderwidth=0)
    gif.place(x=-150, y=-300)
    window2.after(0, update, 0)

    def encrypt2():
        text = text_box1.get(1.0, END)
        text_box2.delete(1.0, END)
        text3 = ''
        for j in range(1, 32):
            key = -j
            text2 = ''
            for i in range(len(text)):
                t = text[i].lower()
                if t in eng_alphabet:
                    s = eng_alphabet.find(t)
                    if s + abs(key) >= len(eng_alphabet):
                        s = (key + s) % len(eng_alphabet)
                        text2 += eng_alphabet[s].upper() if text[i].isupper() else eng_alphabet[s]
                    else:
                        s += key
                        text2 += eng_alphabet[s].upper() if text[i].isupper() else eng_alphabet[s]
                elif t in rus_alphabet:
                    s = rus_alphabet.find(t)
                    if s + abs(key) >= len(rus_alphabet):
                        s = (key + s) % len(rus_alphabet)
                        text2 += rus_alphabet[s].upper() if text[i].isupper() else rus_alphabet[s]
                    else:
                        s += key
                        text2 += rus_alphabet[s].upper() if text[i].isupper() else rus_alphabet[s]
                else:
                    text2 += text[i]
            text3 += f' \n{text2} (key: {key})\n'
        text_box2.insert(1.0, text3)

    Label(window2,
          text="Caesar's Pawn",
          font='AdobeFangsongStd-Regular 30',
          fg='#32CD32',
          bg='black'
          ).pack(side=TOP)

    Label(window2,
          text='Encrypt mode',
          font='AdobeFangsongStd-Regular 15',
          fg='#32CD32',
          bg='black'
          ).place(x=240, y=45)

    Label(window2,
          text='Encrypted text                             Decrypted text',
          font='AdobeFangsongStd-Regular 15',
          fg='#32CD32',
          bg='black'
          ).place(x=80, y=120)

    def paste_text():
        OpenClipboard()
        p = GetClipboardData()
        text_box1.delete(1.0, END)
        text_box1.insert(1.0, p)

    Button(window2,
           text='Paste',
           command=paste_text,
           fg='#32CD32',
           bg='black',
           font='AdobeFangsongStd-Regular',
           activebackground='#32CD32',
           activeforeground='black',
           relief='ridge',
           cursor="hand2"
           ).place(x=17, y=118)

    Button(window2,
           text='-->',
           command=encrypt2,
           fg='#32CD32',
           bg='black',
           font='Arial 13',
           activebackground='#32CD32',
           activeforeground='black',
           relief='ridge',
           cursor="hand2"
           ).place(x=283, y=120)

    text_box1 = Text(window2,
                     width=32,
                     height=31,
                     fg='#32CD32',
                     bg='black',
                     relief='sunken',
                     font=('Times New Roman', 13))
    text_box1.pack(side=LEFT, anchor=S)

    text_box2 = Text(window2,
                     width=32,
                     height=31,
                     fg='#32CD32',
                     bg='black',
                     relief='sunken',
                     font=('Times New Roman', 13))
    text_box2.pack(side=RIGHT, anchor=S)

    window2.mainloop()


Button(window,
       text='Encrypt mode',
       command=encrypt_window,
       fg='#FFD700',
       bg='#8B0000',
       font='AdobeFangsongStd-Regular',
       activebackground='#8B0000',
       activeforeground='#FFD700',
       cursor="hand2"
       ).place(x=323, y=135)

Button(window,
       text='Confirm',
       command=encrypt,
       fg='#FFD700',
       bg='#8B0000',
       font='AdobeFangsongStd-Regular',
       activebackground='#8B0000',
       activeforeground='#FFD700',
       cursor="hand2"
       ).place(x=5, y=135)


def copy():
    text_box.clipboard_clear()
    text_box.clipboard_append(text_box.get(1.0, END))


Button(window,
       text='Copy',
       command=copy,
       fg='#FFD700',
       bg='#8B0000',
       font='AdobeFangsongStd-Regular',
       activebackground='#8B0000',
       activeforeground='#FFD700',
       cursor="hand2",
       relief='groove'
       ).place(x=-1, y=290)

Checkbutton(window,
            text='Encrypt',
            var=encrypt_state,
            fg='#FFD700',
            bg='#8B0000',
            font='AdobeFangsongStd-Regular',
            selectcolor='#8B0000',
            activebackground='#8B0000',
            activeforeground='#FFD700'
            ).place(x=85, y=135)

text_box = Text(
    width=50,
    height=6,
    fg='#FFD700',
    bg='#8B0000',
    font=('Times New Roman', 13))
text_box.place(x=0, y=180)


def open_author(event):
    open_new("https://www.youtube.com/watch?v=Nx-ZFAgIWzI")


link = Label(window,
             text="By TakPlintus",
             fg="#FFD700",
             font='AdobeFangsongStd-Regular',
             cursor="hand2",
             bg='#8B0000')
link.place(x=348, y=292)
link.bind('<Button-1>', open_author)

window.mainloop()
