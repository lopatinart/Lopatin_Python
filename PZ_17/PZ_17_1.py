# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу

import tkinter as tk
from tkinter import ttk

# Создание главного окна
root = tk.Tk()
root.title("Testform")
root.geometry("700x400")

# Заголовок
title_label = tk.Label(root, text="Testform", fg="black", font=("Arial", 14))
title_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=5)

# Поле имени
tk.Label(root, text="Name").grid(row=1, column=0, sticky="w", padx=10, pady=5)
name_entry = tk.Entry(root, bg="lightgray")
name_entry.grid(row=1, column=1, sticky="w", padx=150, pady=5)

# Поле пароля
tk.Label(root, text="Password").grid(row=2, column=0, sticky="w", padx=10, pady=5)
password_entry = tk.Entry(root, show="*", bg="lightgray")
password_entry.grid(row=2, column=1, sticky="w", padx=150, pady=5)

# Пол
tk.Label(root, text="Gender").grid(row=3, column=0, sticky="w", padx=10, pady=5)
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1, sticky="w", padx=150, pady=2)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=4, column=1, sticky="w", padx=150, pady=2)

# Континент
tk.Label(root, text="Continent").grid(row=5, column=0, sticky="w", padx=10, pady=5)
continent_var = tk.StringVar()
continent_combo = ttk.Combobox(root, textvariable=continent_var, values=["Please select...", "Africa", "Asia", "Europe", "North America", "South America", "Australia", "Antarctica"], state="readonly")
continent_combo.grid(row=5, column=1, sticky="w", padx=150, pady=5)
continent_combo.current(0)

# Питание
tk.Label(root, text="Meals").grid(row=6, column=0, sticky="w", padx=10, pady=5)
breakfast_var = tk.IntVar()
lunch_var = tk.IntVar()
dinner_var = tk.IntVar()
tk.Checkbutton(root, text="breakfast", variable=breakfast_var).grid(row=6, column=1, sticky="w", padx=150, pady=2)
tk.Checkbutton(root, text="lunch", variable=lunch_var).grid(row=7, column=1, sticky="w", padx=150, pady=2)
tk.Checkbutton(root, text="dinner", variable=dinner_var).grid(row=8, column=1, sticky="w", padx=150, pady=2)

# Замечания
tk.Label(root, text="Remark").grid(row=9, column=0, sticky="nw", padx=10, pady=5)
remark_text = tk.Text(root, height=3, width=30, bg="lightgray")
remark_text.grid(row=9, column=1, rowspan=2, sticky="nsew", padx=150, pady=5)

# Кнопки
button_frame = tk.Frame(root)
button_frame.grid(row=12, column=0, columnspan=2, pady=10, sticky="e")
cancel_button = tk.Button(button_frame, text="Cancel", bg="lightgray", bd=2, relief="flat")
cancel_button.pack(side="right", padx=5)
send_button = tk.Button(button_frame, text="Send", bg="lightgray", bd=2, relief="flat")
send_button.pack(side="right", padx=5)

# Настройка веса столбцов и строк
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
root.grid_rowconfigure(9, weight=1)

# Запуск приложения
root.mainloop()