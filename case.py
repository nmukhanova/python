#тема: Разработка методики расчёта эффективности маркетинговых акций АО «Международный аэропорт Сочи»

#интерфейс
import tkinter as tk
 
window = tk.Tk()
window.title("Расчёт эффективности маркетинговых акций")
window.geometry('1024x1024')
window["bg"] = "#f0f8ff"

'''
первый этап - ввод исходных данных:
количество участников акции план/факт
конверсия план/факт
средний чек план/факт
коэффициент транзакции план/факт
'''
def mycom ():
	e = edit.get()

label_a = tk.Label(text = "Введите исходные данные для расчёта", bg = "#f0f8ff", font = ("Arial Bold", 40))
label_a.pack()

#участники
label_b = tk.Label(text = "Количество участников акции", bg = "#f0f8ff", font = ("Arial", 28))
label_b.pack()

edit = tk.Entry (window, width = 20, bg = 'white')
edit.pack()

button1 = tk.Button (window, text = 'Вычислить', command = mycom)
button1.pack()

#конверсия

label_c = tk.Label(text = "Коэффициент конверсии", bg = "#f0f8ff", font = ("Arial", 28))
label_c.pack()

edit1 = tk.Entry (window, width = 20, bg = 'white')
edit1.pack()

button2 = tk.Button (window, text = 'Вычислить', command = mycom)
button2.pack()

#средний чек
label_c = tk.Label(text = "Средний чек", bg = "#f0f8ff", font = ("Arial", 28))
label_c.pack()

edit1 = tk.Entry (window, width = 20, bg = 'white')
edit1.pack()

button2 = tk.Button (window, text = 'Вычислить', command = mycom)
button2.pack()

#транзакции
label_c = tk.Label(text = "Коэффициент транзакции", bg = "#f0f8ff", font = ("Arial", 28))
label_c.pack()

edit1 = tk.Entry (window, width = 20, bg = 'white')
edit1.pack()

button2 = tk.Button (window, text = 'Вычислить', command = mycom)
button2.pack()

window.mainloop()


'''
второй этап - расчёт затрат на проведение акции
сложить постоянные и переменные затраты
'''

'''
третий этап - расчёт выручки
умножить количество участников на средний чек
'''

'''
четвертый этап - расчёт прибыли
перемножить лиды, коэффициент конверсии, средний чек и коэффициент транзакции
'''

'''
пятый этап - расчёт точки безубыточности
сложить постоянные и переменные затраты
'''

'''
шестой этап - расчёт ROMI
(прибыль - затраты на акцию)/затраты на акцию * 100
'''

'''
если ROMI < 100, акция неэффективна
иначе если ROMI > 100, акция эффективна
'''


