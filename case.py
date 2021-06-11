#тема: Разработка методики расчёта эффективности маркетинговых акций АО «Международный аэропорт Сочи»

from tkinter import *

#главная страница: фоновое изображение + кнопка "Начать"
def mainWindow1():
    root = Tk()
    root.resizable(width = False, height = False)
    root.geometry('1400x1024')
    root.title("Расчёт эффективности маркетинговых акций")
    root.iconbitmap( '/Users/user/Desktop/test/aircraft.ico' )
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
                        font = ('Arial Bold', 20),
                        command = butCallback )
    but1.pack(padx = 555, pady = 400, side = BOTTOM)
    root.mainloop()

#второе окно: ввод исходных данных
def mainWindow2():
    root = Tk()
    root.resizable(width = False, height = False)
    root.geometry('1400x1024')
    root.title("Расчёт эффективности маркетинговых акций")
    root.iconbitmap( '/Users/user/Desktop/test/aircraft.ico' )
    root["bg"] = "white"

    frame = Frame(root)
    frame.pack()

    '''
    здесь и далее должны были быть подписи для полей ввода значений, но через pack это выглядит ужасно, а grid не работает
    ml = Label(frame, text = 'Количество участников', font = ('Arial Bold', 20), fg = 'black')
    ml.pack(side = 'left')
    '''
    members = Entry(root, font = ('Arial 20'), fg = 'black',bg = '#CEECF5', relief = 'raised', justify = 'left', show = '')
    members.pack()

    #cl = Label(frame, text = 'Коэффициент конверсии', font = ('Arial Bold', 20), fg = 'black')
    #cl.pack(side='left')
    conversion = Entry(root, font = ('Arial 20'), fg = 'black',bg = '#CEECF5', relief = 'raised', justify = 'left', show = '')
    conversion.pack()

    #bl = Label(frame, text = 'Средний чек', font = ('Arial Bold', 20), fg = 'black')
    #bl.pack(side = 'left')
    bill = Entry(root, font = ('Arial 20'), fg = 'black',bg = '#CEECF5', relief = 'raised', justify = 'left', show = '')
    bill.pack()

    #tl = Label(frame, text = 'Коэффициент транзакции', font = ('Arial Bold', 20), fg = 'black')
    #tl.pack(side = 'left')
    transaction = Entry(root, font = ('Arial 20'), fg = 'black',bg = '#CEECF5', relief = 'raised', justify = 'left', show = '')
    transaction.pack()


    #fcl = Label(frame, text = 'Постоянные затраты', font = ('Arial Bold', 20), fg = 'black')
    #fcl.pack(side = 'left')
    fc = Entry(root, font = ('Arial 20'), fg = 'black',bg = '#CEECF5', relief = 'raised', justify = 'left', show = '')
    fc.pack()

    #vcl = Label(frame, text = 'Переменные затраты', font = ('Arial Bold', 20), fg = 'black') 
    #vcl.pack(side = 'left')
    vc = Entry(root, font = ('Arial 20'), fg = 'black',bg = '#CEECF5', relief = 'raised', justify = 'left', show = '')
    vc.pack()

    def cost_calculator():
        cost = float(fc.get()) + float(vc.get())
        print(cost)
    button_calc1 = Button(root, text="Расчет затрат", command=cost_calculator)
    button_calc1.pack()

    def revenue_calculator():
        revenue = float(members.get()) * float(bill.get())
        print(revenue)
    button_calc2 = Button(root, text="Расчет выручки", command=revenue_calculator)
    button_calc2.pack()

#здесь должна была быть одна кнопка "далее" и вывод расчетов в новом окне, но тоже не получилось
    def profit_calculator():
        profit = float(members.get()) * float(conversion.get()) * float(bill.get()) * float(transaction.get())
        print(profit)
    button_calc3 = Button(root, text="Расчет прибыли", command=profit_calculator)
    button_calc3.pack()

    def bep_calculator():
        bep = float(fc.get()) + float(vc.get())
        print(bep)
    button_calc4 = Button(root, text="Расчет точки безубыточности", command=bep_calculator)
    button_calc4.pack()


    def romi_calculator():
        romi = (float(members.get()) * float(conversion.get()) * float(bill.get()) * float(transaction.get())) - (float(fc.get()) + float(vc.get())) / (float(fc.get()) + float(vc.get()) * 100)
        print(romi)
    btn = Button(root, text="Расчет ROMI", command=romi_calculator)
    btn.pack()

    root.mainloop()

   
if __name__ == '__main__':
    mainWindow1()

'''
для справки
cost(затраты) = fc + vc
revenue(выручка) = members * bill
profit(прибыль) = members * conversion * bill * transaction
break_even_point(точка безубыточности) = fc + vc
ROMI = ((revenue - cost)/cost) * 100
'''