#тема: Разработка методики расчёта эффективности маркетинговых акций АО «Международный аэропорт Сочи»

from tkinter import *
from tkinter import messagebox

#первая страница: фоновое изображение + кнопка "Начать"
def mainWindow1(*w,**kw):
    root = Tk()
    root.resizable(width = False, height = False)
    root.geometry('1400x1024')
    root.title("Расчёт эффективности маркетинговых акций")
    root.iconbitmap( '/Users/user/Desktop/test/plane.ico' ) #почему-то не отображается иконка приложения
    background = Canvas(root)
    filename = PhotoImage(file = "/Users/user/Desktop/test/Расчёт эффективности маркетинговых акций.png")
    background_label = Label(root, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background.pack()
    def butCallback():
        root.destroy()
        mainWindow2()

    but1 = Button(root,
                        text = "Начать",
                        font = 'Arial 20',
                        command = butCallback )
    but1.pack(padx = 555, pady = 400, side = BOTTOM)
    root.mainloop()

'''
первый этап - ввод исходных данных:
количество участников акции план/факт
конверсия план/факт
средний чек план/факт
коэффициент транзакции план/факт
постоянные затраты план/факт
переменные затраты план/факт
'''
def mainWindow2(*w,**kw):
    root = Tk()
    root.resizable(width = False, height = False)
    root.geometry('1400x1024')
    root.title("Расчёт эффективности маркетинговых акций")
    root.iconbitmap( '/Users/user/Desktop/test/plane.ico' )
    root["bg"] = "white"

    def check(event):
        M = members.get()
        C = conversion.get()
        B = bill.get()
        T = transaction.get()
        F = fc.get()
        V = vc.get()

        if not M and not C and not B and not T and not F and not V:
            messagebox.showerror('Error', 'Введите данные!')  
        elif not M and C and B and T and F and V:
            messagebox.showerror('Error', 'Введите данные!')
        elif not C and M and B and T and F and V:
            messagebox.showerror('Error', 'Введите данные!')
        if M and C and B and T and F and V:
            def butCallback():
                root.destroy()
                mainWindow3()
            but1 = Button(root, text ="Выполнить расчет",
                font = ('Arial Bold', 20), command = butCallback )    
            but1.pack(padx = 555, pady = 400, side = BOTTOM)  
            text1 = Text(root)    
            text1.pack()
            root.mainloop() 

    text_members = Label(text = 'Количество участников', font = ('Arial Bold', 20), 
        fg = 'black')

    members = Entry(root, font = ('Arial Bold', 20),
        fg = 'black',bg = '#CEECF5',
        relief = 'raised',
        justify = 'left',
        show = '')


    text_conversion = Label(text = 'Коэффициент конверсии', font = ('Arial Bold', 20), 
        fg = 'black')
    conversion = Entry(root, font = 'Arial 20',
        fg = 'black', bg = '#CEECF5',
        relief = 'raised',
        justify = 'left',
        show = '')

    text_bill = Label(text = 'Средний чек', font = ('Arial Bold', 20), 
        fg = 'black')
    bill = Entry(root, font = 'Arial 20',
        fg = 'black',bg = '#CEECF5',
        relief = 'raised',
        justify = 'left',
        show = '')

    text_transaction = Label(text = 'Коэффициент транзакции', font = ('Arial Bold', 20), 
        fg = 'black')
    transaction = Entry(root, font = 'Arial 20',
        fg = 'black',bg = '#CEECF5',
        relief = 'raised',
        justify = 'left',
        show = '')

    text_fc = Label(text = 'Постоянные затраты', font = ('Arial Bold', 20), 
        fg = 'black')
    fc = Entry(root, font = 'Arial 20',
        fg = 'black',bg = '#CEECF5',
        relief = 'raised',
        justify = 'left',
        show = '')

    text_vc = Label(text = 'Переменные затраты', font = ('Arial Bold', 20), 
        fg = 'black')
    vc = Entry(root, font = 'Arial 20',
        fg = 'black',bg = '#CEECF5',
        relief = 'raised',
        justify = 'left',
        show = '')

    enter = Button(text = 'Выполнить расчет', font = ('Arial Bold', 20),
        fg = 'black',
        relief = 'raised',
        activebackground = '#CEECF5',
        activeforeground = 'black')


    text_members.pack()
    members.pack()
    text_conversion.pack()
    conversion.pack()
    text_bill.pack()
    bill.pack()
    text_transaction.pack()
    transaction.pack()
    text_fc.pack()
    fc.pack()
    text_vc.pack()
    vc.pack()
    enter.pack()

    enter.bind('<Button-1>', check)
    root.mainloop()

'''
второй этап - вывод результатов (план/факт)
затраты = постоянные + переменные
выручка = количество участников * средний чек
прибыль = лиды * конверсия * средний чек * к-т транзакции
точка безубыточности = постоянные + переменные затраты
ROMI = (прибыль - затраты на акцию)/затраты на акцию * 100

если ROMI < 100, акция неэффективна
иначе если ROMI > 100, акция эффективна
подсветить красным, если плановые показатели не равны фактическим
'''
def mainWindow3(*w,**kw):
    root = Tk()
    root.resizable(width = False, height = False)
    root.geometry('1400x1024')
    root.title("Расчёт эффективности маркетинговых акций")
    root.iconbitmap( '/Users/user/Desktop/test/plane.ico' )
    root["bg"] = "white"

    root.mainloop()
    
if __name__ == '__main__':
    mainWindow1()
