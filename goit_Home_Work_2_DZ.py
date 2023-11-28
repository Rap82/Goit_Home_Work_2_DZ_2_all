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

# import math # підключення вбудованої Python  бібліотеки *math .
  
# a = int (input("Enter coefficient a: "))     # змінній *а присвоюємо значення введене з клавіатури приведена до типу *int( цілі числа )

# if a !=0 :                                   # перевірка . Якщо ввели 0 то це не буде кавдратне рівнння згідно визначення про нього. Переходимо відразу на else:
#     b = int (input("Enter coefficient b: ")) # якщо в недрівнює 0 виконуємо тіло умови. Просимо вести значення *в .ВВедене значення приводимо до типу *int
#     c = int (input("Enter coefficient c: ")) # Просимо вести значення *c ВВедене значення приводимо до типу *int

#     riv=f"{a}x**2+{b}x+{c}"                 # в зміну riv присвоюємо значення f-рядка в якому буде записано замість {a}, {b}, і {c} конкретні значеня ведені користувачем з клавіатури.
#     D = b**2-4*a*c                          # зміна D - детермінанта. Потрібна для розрахунку кавдратнго рівнняє . визначається формулою " D = b**2-4*a*c " де b**2 -запис піднесення до стапіння 2 (квадрат чила ) ( b - змінна яку підносимо в степінь , ** - запис піднесення до степіння , 2 - степінь до якого підносимо )
    
#     #  В залежності від значення D (детермінанти) квадратне рівняння може мати різні рішення. Нижче робимо перевірку на ці умови.
    
#     if D > 0 :   # якщо D більше 0 кавдратне рявння має два дійсних корення x1 і x2                            
#         x1 = (-b + math.sqrt(D)) / (2 * a) # присвоюємо x1 значення розраховане формулою (-b + math.sqrt(D)) / (2 * a) - де math.sqrt(*число чи змінна зякої добуваємо корінь*) - стандартна функція бібліотеки *math  , повертає значення корення з числа .В нашому випадку корінь з D (детермінанти)
#         x2 = (-b - math.sqrt(D)) / (2 * a) # присвоюємо x2 значення розраховане формулою (-b - math.sqrt(D)) / (2 * a) - де math.sqrt(*число чи змінна зякої добуваємо корінь*) - стандартна функція бібліотеки *math  , повертає значення корення з числа .В нашому випадку корінь з D (детермінанти)
#         print(f"Рівняння {riv} має один 2 дійсний корення x1 = {x1} , x2 = {x2} ") # виводимо - *Рівння {riv}-підствляє значення зміної riv* має 2 дійсних корення x1 = *{x1}- замість {x1} підствляє значення зміної x1* , x2 = *{x2} - замість {x2} підствляє значення зміної x2*
    
#     elif D==0 :                             # або якщо D дорівнює 0 , кавдратне рявння має один дійсний корінь x1
#         x1 = (-b + math.sqrt(D)) / (2 * a)  # присвоюємо x1 значення розраховане формулою (-b + math.sqrt(D)) / (2 * a)
#         print(f"Рівняння {riv} має один l дійсний корінь x1 = {x1}") # виводимо - Рівння *{riv}-підствляє значення зміної riv* має 1 дійсниq корінь x1 = *{x1}- замість {x1} підствляє значення зміної x1* 
    
#     else:                                               # *else  інакше  D <0 (у всіх інших випадках )  . 
#         print(f"Рівння {riv} немає дійсних коренів .")  # виводимо - Рівння *{riv}-підствляє значення зміної riv* немає дійсних коренів .

# else:                                                   # *else  інакше для умови *if a !=0 :* 
#     print("це не квадратне рівння")                     # виводимо - це не квадратне рівння



# =======================  Завдання 6/Task_6  ==================

#++++++++++++++++++++++++ Умова/Condition   +++++++++++++++++++++++

#++++++++++ Визначити парне число чи ні, за допомогою тернарного оператора. ++++++++++++++++++

# Програма встановлює значення змінної is_even у True або False, залежно від того, чи є число в змінній num парним або непарним.

# Підказка: перевірка на парність виконується порівнянням залишку від поділу на 2 з 0 або 1.
# Нагадаємо, залишок від ділення можна отримати після операції %

# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++

# num = int ( input ("Enter an integer number: ") ) #  змінній *num присвоюємо значення введене з клавіатури приведена до типу *int( цілі числа )
# ostacha = num % 2                                 #  змінній *ostacha присвоюємо значення остачі від ділення веденого числа в *num на 2 . якщо остача рівна 0 значить число парне (ділиться на 2 без остачі) в інших випадках непарне.

# is_even = False if ostacha else True              #  запис тернарного оператора ( це коли зміній на початку рядка присвоюмо різні значення в залежності від того чи виконується одна чи інша умова ) 
#                                                   #  в нашому випадку змінії  *is_even  буде прсивоєно *False якщо зміна  *ostacha дорівнює 0 (0 в умові if інтерпретується як занчення *False) у всіх інших випадках *else : змінії *is_even присвоється начення *True  

# if is_even :                                      # Перевіряємо чи число парне(even).Якщо *is_even == True . Число введене в *num - парне
#     print(f" {num} - Even ")                      # виводимо - {num} * замість {num}- підствляє значення зміної num*  - Even
# else:                                             # *else  інакше для умови *if is_even :* в нашому випадку тоді  *is_even == False
#     print(f" {num} - Odd")                        # виводимо - {num} * замість {num}- підствляє значення зміної num*  - Odd


# =======================  Завдання 7/Task_7  ==================

#+++++++++++++++++++++++  Цикл while +++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Цикл while - запис  while *умова : - виконується доти поки *умова є True .
# Використовується якщо наперед невідомо скількі раз потрібно виконувати код який розміщений в тілі циклу (все що зміщено вправо більше ніж на 4 пробіли/tab від початку запису while) 
# Може приводити до безкінечного циклу .
# Щоб уникнути безкінечності обовязково потрібно приводити умову циклу while в значення *False  коли більше непотрібно виконувати тіло циклу while 
# або переривати цикл оператаром *break
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++ Умова/Condition   +++++++++++++++++++++++

# Користувач вводить число від 0 до 100. Підрахуйте, використовуючи цикл while, 
# суму всіх чисел від першого до введеного числа включно в num. Результат помістити в змінну sum.

# Тести будуть:

# Поміщати тестові значення для змінної num: 20, 10, 5, 100

# І чекати суми в змінній sum: 210, 55, 15, 5050

# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++
# Для вирішення задачі будемо додавати всі числа від значення num до 0,
# зменшуючи num на одиницю . *num-1*  щоб обрахувати суму всіх чисел згідно умови задачі.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# num = int ( input ("Enter the integer (0 to 100): ") )  # змінній *num присвоюємо значення введене з клавіатури приведена до типу *int( цілі числа )
# sum = 0                                                 # змінній *sum присвоюємо початкове значення 0 .в зміна *sum буде використана для запису суми всіх чисел від 0 до занчення *num

# while num >= 0 :    # Цикл while з умовою num більше-рівне 0 буде виконуватись поки *num не стане менше 0.Для того ми від num віднімаєм одиницю зменшучи значення на одиницю від попереднього на кжному кроці циклу і так поки нам нестане менше 0 
#     sum += num      # sum += num  те саме що sum = sum + num (різні записи одного і того самого виразу ). в зміну *sum переприсвоюєм  попереднє значення *sum + поточне значення *num . # приклад Якщо *num == 10 то *sum == 10 + 0 на першому кроці. на наступному  *sum == 10 + 9 на наступному *sum == 19 + 8 і так далі.
#     num -= 1        # num -= 1    те саме що sum = sum - 1   (різні записи одного і того самого виразу ). в зміну *num переприсвоюєм  попереднє значення *num - 1 . # приклад Якщо *num == 10 то на дрігому  кроці *num == 9 , на наступному  *num == 8 , на наступному  *num == 7 і так дальше поки *num не стане менше 0 тоді цикл while зупиниться оскільки умова *num >= 0* стане Fasle


# =======================  Завдання 8/Task_8  ==================

#+++++++++++++++++++++++  Цикл * for in : * +++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Цикл for - запис  for  *зміна*  in  *діапазон знаначень*  : - виконується доти поки незакінчиться останє значення з діапазону виконуючи тіло циклу на кожному значенні з діапазону .
# Використовується якщо наперед відомо скількі раз потрібно виконувати код який розміщений в тілі циклу (все що зміщено вправо більше ніж на 4 пробіли/tab від початку запису for) 
# Діапазон задається або за допомогою оператора range (*з якого значення почати , * яким значенням закінчити (де останнє значення не враховується))
# або значенням яке має чітко виражений  початок і кінець значень.Ітерабельний об’єкт.Приклад : списки , кортежі , словники , множини , та рядки

# Цикл for можна використати, щоб ітерувати над ітерабельним об’єктом декілька разів.
# Ітерабельним об’єктом у Python є будь-який об’єкт, який можна використати у послідовності та над яким можна виконати цикл.
# У Python існує безліч ітерабельних об’єктів, а до найпоширеніших належать:
# списки , кортежі , словники , множини , та рядки
# Цикл for ітерує над кожним елементом у послідовності по порядку.

# Він також виконує однаковий блок коду для кожного елемента.
# Завдяки цій поведінці цикл for корисний, якщо:
# ви знаєте скільки разів потрібно виконати блок коду;
# ви хочете виконати однаковий код для кожного елемента у наданій послідовності.

# Можна переривати цикл оператаром *break - якщо непотрібно більше виконувати тіло циклу і завершити цикл for достроково (до моменту завршення циклу (поки недійшло до сотанього елементу з вказаного діапазону)).
# оператор *continue - застосовується якщо потрібно взяти наступне значення з діапазону циклу . все що нижче оператора *continue в циклі не виконується .
# Оператор *continue - є зміст встанолюватив тілі умови яка якщо виконоються , то непотрібно нічого виконувати а взяти наступне занчення з діапазону.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++ Умова/Condition   +++++++++++++++++++++++

# Рядок — це об'єкт, що ітерується, а, значить, ми можемо використовувати його в циклі for.
# Підрахуйте в заданому рядку message кількість входжень символу зі змінної search. Результат помістіть у змінну result.

# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++


# message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience." # зміній *message присвоюєм значення типу *str(рядок/стрічка) , Ця зміна це рядок в якому будемо шукати .
# search = "r" # зміній *search присвюємо значення *str(рядок/стрічка) -внашому випадку це це символ "r"  . зміна search - це зміна значення якої будемо шукати в рядку *message
# result = 0   # голошуємо зміну *result . Зміна в яку будемо переприсвоювати значення відповдно до кількості входжень значення *search  в занчення *message .початкове значення 0 .Входжень не виявлено.
# for char in message :   # в циклі *char in message :* буде зміній  *char присвоюватись нове значення символа з рядка  *message на кожному кроці виконання циклу аж поки рякод *message не закінчиться.
#                         # Приклад : На першому кроці char == "N" ,на наступному  char == "e" ,на наступному  char == "v" , і так дальше  на останьому кроці char == "." . *char- буде набувати всіх значень рядка *message покроково.(всі символи цифри,карпки пробіли і інші розділові знаки також є елементами рядка )
#     if char == search : # Перевіряємо умову . *if char == search :*  Якщо *char на якомусь кроці буде дорівнювати *search(значення яке шукаємо в рядку *message) то додаэмо до значення *result одиницю .
#         result += 1     # якщо умова *if char == search :* виконалась (True) , збіг знайдений , збільшуємо наш лічильник *result на одиницю. В кінці *result буде містити значення рівне кількості збігів згідно умови.

# print (f"\nВ рядку {message} \nзнайдено: {result} - символів: {search}") # Виводимо повідомлення на екран відповідно до умови задачі. символ \n -це службовий символ - переносить вивід з наступного рядка всього що стоїть пілся нього.


# =======================  Завдання 9/Task_9  ==================

#++++++++++++++++++++++++ Алгоритм виішення : +++++++++++++++++++
# Хай є два початкових числа first та second.
# Виберемо менше з них та привласнимо значення змінній gcd.
# Поки first або second не діляться на gcd без залишку, треба виконувати цикл, в якому зменшуємо змінну gcd на одиницю.
# Коли цикл закінчиться в змінній gcd буде НСД для чисел first та second
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++ Умова/Condition   +++++++++++++++++++++++

# Напишіть програму, яка для двох додатних цілих чисел знаходить НСД.
# На співбесідах часто люблять запитувати про алгоритми. Наприклад, розрахуйте найбільший спільний дільник (НД) двох додатних чисел.
# НСД — це найбільше число, на яке без залишку діляться обидва числа.

# Є кілька алгоритмів знаходження НСД, але ми розберемо циклічний алгоритм
# Примітка: Для умови циклу в пункті 3 необхідно пам'ятати, що цикл while виконується за умови True, 
# а наш цикл повинен закінчитися, тільки якщо gcd поділив обидва числа без залишку.

# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++


# first = int ( input("Enter the first integer: ") )   # *first присвоюємо значення введене з клавіатури приведене до типу *int
# second = int ( input("Enter the second integer: ") ) # *second  присвоюємо значення введене з клавіатури приведене до типу *int

# if first >= second : # Перевріка чи *first більше за *second .
#     gcd = second     # якщо умова *first >= second :* виконалась   то *second значить мениший-рівний  за *first  тоді *gcd = second (присвоюємо менше з двох значень в *gcd )
# else:                # інакше (коли не виконується умова *first >= second :*) *second значить ,більший  за *first
#     gcd = first      # *gcd = first (присвоюємо менше з двох значень в *gcd )

# while gcd > 0 :      # цикл while в якому будемо на кожному кроці шукати остачу від ділення  значеннь first і second на gcd і зменшувати *gcd на одиницю .Є дві умови завершення циклу :
#                      # Початкова  *gcd > 0* для завершення циклу якщо жодне з значень не задівільнить умову в середені циклу. Тоді НДС є 1.
#                      # Додаткова умова в тілі циклу  *if ost_first == 0 and ost_second == 0 :* якщо вона виконається занчить поточне значення *gcd є НДС для цих значень . Тоді виходимо з циклу задопомогою оператора  *break
    
#     ost_first = first % gcd    # в зміну *ost_first записумо остачу від ділення first на  gcd . Оператор " % " - повретає остачу від ділення  , значення  з ліва від нього, на  ,значення з права від нього .
#     ost_second = second % gcd  #  в зміну *ost_second записумо остачу від ділення second на  gcd . Оператор " % " - повретає остачу від ділення  , значення  з ліва від нього, на  ,значення з права від нього .
#     if ost_first == 0 and ost_second == 0 : # Умова де перевіряємо чи остача на *gcd першого і другого значення рівна 0 . якщо так то поточне значення  *gcd є наш НДС для цих двох значень.
#         #print(gcd)
#         break                        # якщо умова *if ost_first == 0 and ost_second == 0 :* виконалась значить завершуємо цикл за допомгою *break . більше нам нічого шукати непотрібно. *gcd буде містити поточне значення при якому додаткова умова виконалась
#     gcd -= 1 # Зменшуємо *gcd на одиницю .Цикл перевіряє чи виконується Початков умова циклу *gcd > 0* для нового значення *gcd ,якщо виконується то виконує повторно код в циклі з зміненим значенням  *gcd(мениши на одиницю від попередього значення) до тих пір поки або не виконається додатково умова в циклі або не виконається початкова умова в циклі.

# print(f" {gcd} Є НДС для чисел {first} і {second} " ) # виводимо на екран стрічку з відповідними записами. де {gcd} - НДС ; {first} і {second} - перше і друге введене з клавіатури значення.


# =======================  Завдання 10/Task_10  ==================
#+++++++++++++++++++++++++++ Вкладений  цикли  *for в цикл *while  +++++++++++++++++++++++++

#++++++++++++++++++++++++ Умова/Condition   ++++++++++++++++++++++

# Напишіть два цикли, вкладені один в один. 
# У першому циклі while ми постійно запитуємо ціле число,
# а у другому з допомогою циклу for складаємо суму чисел від 0 до введеного числа включно і додаємо до змінної sum. 
# Змінна sum накопичує суми, що утворюються при кожному введенні числа. Вихід з першого циклу здійснюємо, якщо ми ввели число 0.

# ++++++++++++++++++++++++++ Запропоновані приклади для обрахунку ++++++++++++++
# використовують дві тестові послідовності чисел:

# 10, 13, 73, 0 і чекають на суму 2847
# 1, 2, 3, 4, 0 і чекають на суму 20
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ++++++++++++++++++++++++   Код/Code   +++++++++++++++++++++++++++++++++++

num = int ( input ("Enter integer (0 for output): ") ) # в *num присвоюємо значення введене з клавіатури приведене до типу *int
sum = 0                                                # оголошуємо *sum з початковим  значення 0 .

while num != 0 :           # рахуємо суму всіх введених чисел з клавіатури . Перше значення  отримуємо ще до початку виконання циклу в самому циклі будемо кожний раз запитувати введення нового числа . після ведення обраховувати суму всіх чисел до введеного добавляючи суму чисел введених до початку циклу. 
                           # Умова завершеня циклу введення числа 0 згідно умови завдання.
    for x in range (num) : # вкладеному циклі for Обраховуємо суму всіх чисел від 0 до введеного числа *num додаючи суму попередьо обрахованого таким же способом числа.
        sum = sum + x + 1  # до суми додаємо поточне значення x з діапазону range (num)(діапазон буде приймати значення від 0 до значення *num (невключаючи значення  num) , для того щоб всетаки значення num було додано до суми ми на кожному кроці циклу for будемо добавляти 1 . в кінці циклу сума дбавлених одиничок буде відповідати числу *num  )
        
    print(sum)             # виводимо на екран поточне значення *sum
    num = int ( input ("Enter integer (0 for output): ") ) # в циклі повторно просимо ввести нове значення яке переприсвоюємо в *num для наступного обрахунку і так до тих пір поки неведуть 0 . 0 умова виходу з циклу while *num != 0 * - буде False якщо *num == 0 .