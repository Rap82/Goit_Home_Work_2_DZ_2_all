#************************Home_Work_2_Go_it*************************

#*********** Керуючі конструкції. Винятки/Control structures. Exceptions **************

 
# =======================  Завдання 1/Task_1  ==================

#++++++++++++++++++++++++ Умова/Condition   +++++++++++++++++++++++

# На технічній співбесіді претенденти на посаду одержують оцінку за тест. 
# У наступний тур співбесіди проходять кандидати, які склали тест на 83 бали включно або вище. 
# Реалізуйте оператор контролю виконання так, щоб він привласнив логічній змінній is_next значення True, 
# якщо кількість набраних балів буде більшою або дорівнює 83. В іншому випадку значення змінної дорівнює False.

# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++

# is_next = None # Оголошуємо зміну *is_next через присвоєння значення *None ( невідомий тип даних)

# num = int(input("Enter the number of points: ")) # просимо вести з клавіатури кількість балів які отримали за тест. Приводимо введені дані до числових .Позаовчуванню input повертає введені дані типу *str(стрічка/рядок)

# if num >= 83 : # переврка чи кількість балів відповідає умові. якщо більше рівне 83 виконуємо тіло умови. # Якщо умова if виконнується (True) тоді виконуться тіло (код розміщений на 4 пробіли/tab вправо від положення if )
#     is_next = True # тіло умови if .  *is_next присвоюємо значення  *True

# else : # якщо умова if невикнується переходимо до *else і виконуємо тіло  *else (код розміщений на 4 пробіли/tab вправо від положення *else )
    
#     is_next = False # тіло умови *else.  *is_next присвоюємо значення  *False


# =======================  Завдання 2/Task_2  ==================

#++++++++++++++++++++++++ Умова/Condition   +++++++++++++++++++++++

# У нас є три логічні змінні.

# Перша визначає статус користувача is_active, яка дорівнює True або False.
# Друга is_admin визначає, чи є у користувача права адміністратора теж булевого типу.
# Третя is_permission — чи дозволено доступ, теж булевого типу.
# Приведіть змінні is_active, is_admin та is_permission до булевого вигляду.

# Надайте змінній access значення, яке покаже, чи є доступ у користувача. Використовуйте логічні оператори.

# Адміністратор завжди має доступ, незалежно від значень змінних is_permission та is_active.

# Користувач має доступ, тільки якщо is_permission дорівнює True та is_active також дорівнює True.

# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++

# is_active = input("Is the user active? y/n ? ") # Просимо вести користувача y чи n і присвоюємо відповідне значення зміній *is_active
# is_admin = input("Is the user administrator? y/n? ") # Просимо вести користувача y чи n і присвоюємо відповідне значення зміній *is_admin
# is_permission = input("Does the user have access? y/n?") # Просимо вести користувача y чи n і присвоюємо відповідне значення зміній *is_permission

# if is_active == "y" :  # Перевірка чи ввели "y" на першому питані ( is_active == "y" )
#     is_active = True   # якщо умова виконується *is_active переприсвоюємо значення *True
# else:                  # якщо умова не виконується ,  увсіх інших випадках крім  , *is_active == "y"
#     is_active = False  # *is_active переприсвоюємо значення *False

# if is_admin == "y" :   # Перевірка чи ввели "y" на другому   питані ( is_admin == "y" )
#     is_admin = True    # якщо умова виконується *is_admin переприсвоюємо значення *True
# else:                  # якщо умова не виконується , увсіх інших випадках крім , *is_admin == "y"
#     is_admin = False   # *is_admin переприсвоюємо значення *False

# if is_permission == "y" : # Перевірка чи ввели "y" на третьому питані ( is_permission == "y" )
#     is_permission = True  # якщо умова виконується *is_permission переприсвоюємо значення *True
# else:                     # якщо умова не виконується , увсіх інших випадках , крім *is_permission == "y"
#     is_permission = False # *is_permission переприсвоюємо значення *False

# access = is_admin or is_active and is_permission # присвоюємо зміній *access значення виконання булевих перації "or"(або) і "and"(і) .Присвоїть *True  якщо хочаб умови is_admin і is_permission  будуть *True в інакшому випадку буде *False


# if access and is_admin :                # перевіряємо чи access *True і *is_admin *True
#     print ("У вас є доступ адміна " )   # якщо умова виконалась виводимо - У вас є доступ адміна 

# elif  is_active  and is_permission  :   # *elif(або) перевірмо чи *is_active == *True і *is_permission == *True
     
#     print("У вас доспуп  корситувача ") # якщо умова *elif(або) виконується виводимо -  У вас доспуп  корситувача 

# else:                                   # у всіх інших випадках 
#     print(f"У доступу відмовлено ")     # виводимо - У доступу відмовлено



# =======================  Завдання 3/Task_3  ==================

#++++++++++++++++++++++++ Умова/Condition   +++++++++++++++++++++++
    
# Як відомо, зазвичай розробників заведено поділяти на три категорії: 
# Джун (Junior) & mdash; молодший спеціаліст, Мідл ( Middle) — основний розробник
# у компанії та Сеньйор (Senior) — старший розробник. Орієнтовно можна вважати, 
# що до 1 року роботи включно — це Джуніор, понад 5 років — це Сеньйор розробник, а від одного року до 5 включно — мідл.

# Є змінна work_experience, що визначає стаж роботи програміста. Залежно від стажу роботи, 
# присвоїти змінній developer_type значення "Junior", "Middle" або "Senior".
# Використовуйте, якщо необхідно, булеві оператори or та and під час перевірок.
    
# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++


# work_experience = int ( input("Enter your full work experience in years: ") ) # *work_experience присвоюємо значення введені з клавіату приведені до типу цілих чисел (*int)

# if  1 < work_experience <= 5 : # Перевіряємо чи введені дані відповідають умові . Більше ніж 1 і менше-рівне 5 
#     developer_type = "Middle"  # якщо умова виконнується присвоюємо *developer_type  значення "Middle"

# elif work_experience <=1 :     # Перевіряємо чи введені дані відповідають умові .  менше-рівне 1 
#     developer_type = "Junior"  # якщо умова виконнується присвоюємо *developer_type  значення "Junior"

# else:                          # у всіх інших випадках  
#     developer_type = "Senior"  # якщо умова виконнується присвоюємо *developer_type  значення "Senior"



# =======================  Завдання 4/Task_4  ==================

#++++++++++++++++++++++++ Умова/Condition   +++++++++++++++++++++++

# Перепишіть приклад із теорії, але для додатного числа перевіряйте — парне воно чи ні. 
# Таким чином після перевірок змінна result повинна містити одне з чотирьох значень:

# "Positive even number"
# "Positive odd number"
# "Negative number"
# "It is zero"
# Підказка: перевірка на парність виконується порівнянням залишку від поділу на 2 з 0 або 1. 
# Нагадаємо, залишок від ділення можна отримати після операції %

# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++

# num = int ( input ("Enter a number: ") ) # num присвоюєм  приведене до *int введене з клавіатури значення.

# if num > 0 :                             # Перевірка чи введене число *num додатнє (більше 0 )
#     if num % 2 == 0 :                    # Перевірка чи введене число *num парне . остача від ділення на 2  дорівнює 0  значить() num - Парне(even) ) . (% -оператр повертає остачу від ділення одного числа наінше)
#         result =  "Positive even number" # зміній result присвоюєм значення "Positive even number" ("Додатнє парне число")

#     else:                                # у всіх інших випадках .
#         result = "Positive odd number"   # зміній result присвоюєм значення "Positive odd number" ("Додатнє не парне число")

# elif num < 0 :                           # Перевірка чи введене число *num відємне  ( менше  0 )
#     result = "Negative number"           # зміній result присвоюєм значення "Negative number" (" Відємне  число")

# else:                                    # у всіх інших випадках . ( якщо число num  ціле і не є більше 0 і менше 0 то це є 0 (дорівнює нулю ))
#     result = "It is zero"                # зміній result присвоюєм значення "It is zero"  (" Це є нуль ")

# print (f'Ви вввели {num}  це {result} ') # виводимо через f- рядок . Ви ввели   *{num}- (підстаяє замість {num} значення введене в num ) це *{result}- (підстаяє замість {result} значення отримана в result в залежносі від того що ввели в num )



# =======================  Завдання 5/Task_5  ==================

#++++++++++++++++++++++++ Умова/Condition   +++++++++++++++++++++++

# +++++++++++++++++++++розрахунку коренів квадратного рівняння  ++++++++++

# Необхідно обчислити корінь квадратного рівняння.

# a · x2 + b · x + c = 0

# Дискримінант рівняння помістіть у змінну D

# D = b2 - 4 · a · c

# Корінь рівняння помістіть у змінні x1 та x2

# x1 = (-b + D0.5) / (2 · a)

# x2 = (-b - D0.5) / (2 · a)

# Минулого разу ми просто вказали значення коефіцієнтів a, b, c. 
# Тепер, коли ми вже знаємо про розгалуження, ми можемо перевіряти значення дискримінанта і, 
# в залежності від того додатне чи від'ємне, провести розрахунок коренів. Виконайте розрахунок коренів 
# для довільних значень коефіцієнтів a, b, c.

# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++

import math # підключення вбудованої Python  бібліотеки *math .
  
a = int (input("Enter coefficient a: "))     # зміннії *а присвоюємо значення введене з клавіатури. 

if a !=0 :                                   # перевірка . Якщо ввели 0 то це не буде кавдратне рівнння згідно визначення про нього. Переходимо відразу на else:
    b = int (input("Enter coefficient b: ")) # якщо в недрівнює 0 виконуємо тіло умови. Просимо вести значення *в .ВВедене значення приводимо до типу *int
    c = int (input("Enter coefficient c: ")) # Просимо вести значення *c ВВедене значення приводимо до типу *int

    riv=f"{a}x**2+{b}x+{c}"                 # в зміну riv присвоюємо значення f-рядка в якому буде записано замість {a}, {b}, і {c} конкретні значеня ведені користувачем з клавіатури.
    D = b**2-4*a*c                          # зміна D - детермінанта. Потрібна для розрахунку кавдратнго рівнняє . визначається формулою " D = b**2-4*a*c "
    
    #  В залежності від значення D (детермінанти) квадратне рівняння може мати різні рішення. Нижче робимо перевірку на ці умови.
    
    if D > 0 :   # якщо D більше 0 кавдратне рявння має два дійсних корення x1 і x2                            
        x1 = (-b + math.sqrt(D)) / (2 * a) # присвоюємо x1 значення розраховане формулою (-b + math.sqrt(D)) / (2 * a) - де math.sqrt(*число чи змінна зякої добуваємо корінь*) - стандартна функція бібліотеки *math  , повертає значення корення з числа .В нашому випадку корінь з D (детермінанти)
        x2 = (-b - math.sqrt(D)) / (2 * a) # присвоюємо x2 значення розраховане формулою (-b - math.sqrt(D)) / (2 * a) - де math.sqrt(*число чи змінна зякої добуваємо корінь*) - стандартна функція бібліотеки *math  , повертає значення корення з числа .В нашому випадку корінь з D (детермінанти)
        print(f"Рівняння {riv} має один 2 дійсний корення x1 = {x1} , x2 = {x2} ") # виводимо - *Рівння {riv}-підствляє значення зміної riv* має 2 дійсних корення x1 = *{x1}- замість {x1} підствляє значення зміної x1* , x2 = *{x2} - замість {x2} підствляє значення зміної x2*
    
    elif D==0 :                             # або якщо D дорівнює 0 , кавдратне рявння має один дійсний корінь x1
        x1 = (-b + math.sqrt(D)) / (2 * a)  # присвоюємо x1 значення розраховане формулою (-b + math.sqrt(D)) / (2 * a)
        print(f"Рівняння {riv} має один l дійсний корінь x1 = {x1}") # виводимо - Рівння *{riv}-підствляє значення зміної riv* має 1 дійсниq корінь x1 = *{x1}- замість {x1} підствляє значення зміної x1* 
    
    else:                                               # *else  інакше  D <0 (у всіх інших випадках )  . 
        print(f"Рівння {riv} немає дійсних коренів .")  # виводимо - Рівння *{riv}-підствляє значення зміної riv* немає дійсних коренів .

else:                                                   # *else  інакше для умови *if a !=0 :* 
    print("це не квадратне рівння")                     # виводимо - це не квадратне рівння