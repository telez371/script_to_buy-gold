import requests
from tkinter import *
from tkinter import messagebox


def on_closing():
    if messagebox.askokcancel("Ты хорошо подумал?", "Ой ну и ладно не очень то и хотелось!"):
        root.destroy()

root = Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
canvas = Canvas(root, width=714, height=415)
canvas.pack()
root.iconbitmap("ico.ico")


foto_1 = PhotoImage(file = "Travian_New.png", palette=True)
canvas.create_image(0,0, anchor =NW, image = foto_1)




def currency_exchange():
    url = f'https://www.cbr-xml-daily.ru/latest.js'
    weather_parameters = {
        'format': 2,
        'M': ''
    }

    response = requests.get(url, params=weather_parameters).text
    data = eval(response)
    EUR_rate = data.setdefault('rates').setdefault('TRY')
    RUR_rate_35 = (1 * 16.7 / EUR_rate)
    return RUR_rate_35


def currency_exchange_35():
    info_1['text'] = f"{round(currency_exchange()* 2)} р."
    id_button1.configure(bg="#F7ECCC", activebackground="#F7ECCC")

def currency_exchange_120():
    info_2['text'] = f"{round(currency_exchange()* 4)} р."
    id_button2.configure(bg="#F7ECCC", activebackground="#F7ECCC")

def currency_exchange_300():
    info_3['text'] = f"{round(currency_exchange()* 8)} р."
    id_button3.configure(bg="#F7ECCC", activebackground="#F7ECCC")

def currency_exchange_700():
    info_4['text'] = f"{round(currency_exchange()* 15)} р."
    id_button4.configure(bg="#F7ECCC", activebackground="#F7ECCC")

def currency_exchange_1800():
    info_5['text'] = f"{round(currency_exchange()* 35)} р."
    id_button5.configure(bg="#F7ECCC", activebackground="#F7ECCC")

def currency_exchange_3500():
    info_6['text'] = f"{round(currency_exchange()* 76)} р."
    id_button6.configure(bg="#F7ECCC", activebackground="#F7ECCC")



root.title('Покупка золота')
root.geometry('714x415')
root.resizable(width=False, height=False)

#Экран 35
frame_bottom1_1 = Frame(root, bg='#EDDB89', bd=4)
frame_bottom1_1.place(relx=0.15, rely=-0.01, relwidth=0.11, relheight=0.07)
info_1 = Label(frame_bottom1_1, text='Цена', bg='#EDDB89', font=10)
info_1.pack()

#Кнопка 35
frame_bottom1 = PhotoImage(file="120.png")
frame_bottom2 = frame_bottom1.subsample(5, 5)
id_button1 = Button(root, image=frame_bottom2, highlightthickness=0, bd=0, command=currency_exchange_35)
id_button1.place(x=97, y=154,relwidth=0.14, relheight=0.07)
id_button1.configure(bg="#F7ECCC", activebackground="#F7ECCC")


#Экран 120
frame_bottom1_2 = Frame(root, bg='#EDDB89', bd=4)
frame_bottom1_2.place(relx=0.44, rely=-0.01, relwidth=0.11, relheight=0.07)
info_2 = Label(frame_bottom1_2, text='Цена', bg='#EDDB89', font=10)
info_2.pack()

#Кнопка 120
frame_bottom4 = PhotoImage(file="120.png")
frame_bottom5 = frame_bottom4.subsample(5, 5)
id_button2 = Button(root, image=frame_bottom5, highlightthickness=0, bd=0, command=currency_exchange_120)
id_button2.place(x=304, y=154,relwidth=0.14, relheight=0.07)
id_button2.configure(bg="#F7ECCC", activebackground="#F7ECCC")

#Экран 300
frame_bottom1_3 = Frame(root, bg='#EDDB89', bd=4)
frame_bottom1_3.place(relx=0.74, rely=-0.01, relwidth=0.11, relheight=0.07)
info_3 = Label(frame_bottom1_3, text='Цена', bg='#EDDB89', font=10)
info_3.pack()

#Кнопка 300
frame_bottom7 = PhotoImage(file="120.png")
frame_bottom8 = frame_bottom7.subsample(5, 5)
id_button3 = Button(root, image=frame_bottom8, highlightthickness=0, bd=0, command=currency_exchange_300)
id_button3.place(x=510, y=154,relwidth=0.14, relheight=0.07)
id_button3.configure(bg="#F7ECCC", activebackground="#F7ECCC")


#Экран 700
frame_bottom1_4 = Frame(root, bg='#EDDB89', bd=4)
frame_bottom1_4.place(relx=0.15, rely=0.46, relwidth=0.11, relheight=0.07)
info_4 = Label(frame_bottom1_4, text='Цена', bg='#EDDB89', font=10)
info_4.pack()

#Кнопка 700
frame_bottom10 = PhotoImage(file="120.png")
frame_bottom11 = frame_bottom10.subsample(5, 5)
id_button4 = Button(root, image=frame_bottom11, highlightthickness=0, bd=0, command= currency_exchange_700)
id_button4.place(x=91, y=345,relwidth=0.14, relheight=0.07)
id_button4.configure(bg="#F7ECCC", activebackground="#F7ECCC")


#Экран 1800
frame_bottom1_5 = Frame(root, bg='#EDDB89', bd=4)
frame_bottom1_5.place(relx=0.44, rely=0.46, relwidth=0.11, relheight=0.07)
info_5 = Label(frame_bottom1_5, text='Цена', bg='#EDDB89', font=10)
info_5.pack()


#Кнопка 1800
frame_bottom13 = PhotoImage(file="120.png")
frame_bottom14 = frame_bottom13.subsample(5, 5)
id_button5 = Button(root, image=frame_bottom14, highlightthickness=0, bd=0, command= currency_exchange_1800)
id_button5.place(x=304, y=345,relwidth=0.14, relheight=0.07)
id_button5.configure(bg="#F7ECCC", activebackground="#F7ECCC")

#Экран 3500
frame_bottom1_6 = Frame(root, bg='#EDDB89', bd=4)
frame_bottom1_6.place(relx=0.73, rely=0.46, relwidth=0.11, relheight=0.07)
info_6 = Label(frame_bottom1_6, text='Цена', bg='#EDDB89', font=10)
info_6.pack()

#Кнопка 3500
frame_bottom16 = PhotoImage(file="120.png")
frame_bottom17 = frame_bottom16.subsample(5, 5)
id_button6 = Button(root, image=frame_bottom17, highlightthickness=0, bd=0, command= currency_exchange_3500)
id_button6.place(x=510, y=345,relwidth=0.14, relheight=0.07)
id_button6.configure(bg="#F7ECCC", activebackground="#F7ECCC")
root.mainloop()





def main():
    root.mainloop()

if __name__ == '__main__':
    main()

