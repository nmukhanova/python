#тема: Разработка методики расчёта эффективности маркетинговых акций АО «Международный аэропорт Сочи»

#интерфейс
import tkinter as tk

'''
первый этап - ввод исходных данных:
количество участников акции план/факт
конверсия план/факт
средний чек план/факт
коэффициент транзакции план/факт
'''
class App(tk.Tk):
	def __init__(self, root=None):
		super().__init__(root)
		group1 = tk.LabelFrame(self, padx=15, pady=10, text="Введите исходные данные для расчёта")
		group1.pack(padx = 10, pady = 5)

		tk.Label(group1, text = "Количество участников").grid(row=0)
		tk.Label(group1, text = "Коэффициент конверсии").grid(row=1)
		tk.Label(group1, text = "Средний чек").grid(row=2)
		tk.Label(group1, text = "Коэффициент транзакции").grid(row=3)
		tk.Entry(group1).grid(row=0, column=1, sticky=tk.W)
		tk.Entry(group1).grid(row=1, column=1, sticky=tk.W)
		tk.Entry(group1).grid(row=2, column=1, sticky=tk.W)
		tk.Entry(group1).grid(row=3, column=1, sticky=tk.W)



		group2 = tk.LabelFrame(self, padx=15, pady=10, text="Расчёт затрат на проведение акции")
		group2.pack(padx = 10, pady = 5)

		tk.Label(group2, text = "Постоянные затраты").grid(row=0)
		tk.Label(group2, text = "Переменные затраты").grid(row=1)
		tk.Entry(group2).grid(row=0, column=1, sticky=tk.W)
		tk.Entry(group2).grid(row=1, column=1, sticky=tk.W)

		group3 = tk.LabelFrame(self, padx=15, pady=10, text="Расчёт выручки")
		group3.pack(padx = 10, pady = 5)

		tk.Label(group3, text = "Количество участников").grid(row=0)
		tk.Label(group3, text = "Средний чек").grid(row=1)
		tk.Entry(group3).grid(row=0, column=1, sticky=tk.W)
		tk.Entry(group3).grid(row=1, column=1, sticky=tk.W)

		group4 = tk.LabelFrame(self, padx=15, pady=10, text="Расчёт прибыли")
		group4.pack(padx = 10, pady = 5)
#тут лучше сделать всплывающее меню
		tk.Label(group4, text = "Количество участников").grid(row=0)
		tk.Label(group4, text = "Коэффициент конверсии").grid(row=1)
		tk.Label(group4, text = "Средний чек").grid(row=2)
		tk.Label(group4, text = "Коэффициент транзакции").grid(row=3)
		tk.Entry(group4).grid(row=0, column=1, sticky=tk.W)
		tk.Entry(group4).grid(row=1, column=1, sticky=tk.W)
		tk.Entry(group4).grid(row=2, column=1, sticky=tk.W)
		tk.Entry(group4).grid(row=3, column=1, sticky=tk.W)

		group5 = tk.LabelFrame(self, padx=15, pady=10, text="Расчёт точки безубыточности")
		group5.pack(padx = 10, pady = 5)
#и тут тоже
		tk.Label(group5, text = "Постоянные затраты").grid(row=0)
		tk.Label(group5, text = "Переменные затраты").grid(row=1)
		tk.Entry(group5).grid(row=0, column=1, sticky=tk.W)
		tk.Entry(group5).grid(row=1, column=1, sticky=tk.W)		
		
		group6 = tk.LabelFrame(self, padx=15, pady=10, text="Расчёт ROMI")
		group6.pack(padx = 10, pady = 5)

		tk.Label(group6, text = "Прибыль").grid(row=0)
		tk.Label(group6, text = "Затраты на акцию").grid(row=1)
		tk.Entry(group6).grid(row=0, column=1, sticky=tk.W)
		tk.Entry(group6).grid(row=1, column=1, sticky=tk.W)

		self.btn_submit = tk.Button(self, text = "Далее")
		self.btn_submit.pack(padx=10, pady=10, side=tk.BOTTOM)

if __name__ == "__main__":
	app = App()
	app.title("Расчёт эффективности маркетинговых акций")
	app.geometry('512x400')
	app["bg"] = "#f0f8ff"
	app.mainloop()

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


