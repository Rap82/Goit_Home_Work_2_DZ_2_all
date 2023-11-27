#************************Home_Work_2_Go_it*************************

#*********** Керуючі конструкції. Винятки/Control structures. Exceptions **************

 
# =======================  Завдання 1/Task_1  ==================

#++++++++++++++++++++++++ Умова/Condition   +++++++++++++++++++++++

# На технічній співбесіді претенденти на посаду одержують оцінку за тест. 
# У наступний тур співбесіди проходять кандидати, які склали тест на 83 бали включно або вище. 
# Реалізуйте оператор контролю виконання так, щоб він привласнив логічній змінній is_next значення True, 
# якщо кількість набраних балів буде більшою або дорівнює 83. В іншому випадку значення змінної дорівнює False.

# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++

is_next = None # Оголошуємо зміну *is_next через присвоєння значення *None ( невідомий тип даних)

num = int(input("Enter the number of points: ")) # просимо вести з клавіатури кількість балів які отримали за тест. Приводимо введені дані до числових .Позаовчуванню input повертає введені дані типу *str(стрічка/рядок)

if num >= 83 : # переврка чи кількість балів відповідає умові. якщо більше рівне 83 виконуємо тіло умови. # Якщо умова if виконнується (True) тоді виконуться тіло (код розміщений на 4 пробіли/tab вправо від положення if )
    is_next = True # тіло умови if .  *is_next присвоюємо значення  *True

else : # якщо умова if невикнується переходимо до *else і виконуємо тіло  *else (код розміщений на 4 пробіли/tab вправо від положення *else )
    
    is_next = False # тіло умови *else.  *is_next присвоюємо значення  *False