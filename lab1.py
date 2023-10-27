# Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом,
# читающимся поблочно),распознает, преобразует и выводит на экран числа по определенному правилу.
# Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь.
# Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
# Регулярные выражения использовать нельзя.
# Вариант 11
# Натуральные числа. Выводит на экран четные числа, начинающиеся с цифры, введенной с клавиатуры.
# Каждое пятое число выводится прописью.
print("Введите цифру 0-9, с которой начинаются числа в файле, которые нужно найти ")
k = input()
while not k.isdigit():
    print("Некорректное значение")
    k = input()
while int(k) > 9:
    print("Введено число, пожалуйста введите цифру 0-9")
    k = input()
f = open('txt1.txt', 'r')
buffer = []
c = 0
dic = {0:'ноль',1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять'}
s = f.read()
for a in s:
    if not a.isdigit():
        if len(buffer) == 0:
            continue
        else:
            number = int(''.join(buffer))
            if number % 2 == 0:
                c += 1
                if c == 5:
                    st = ""
                    for i in str(number):
                        st = st + dic.get(int(i)) + " "
                    print(st)
                    c = 0
                else:
                    print(number)
            buffer.clear()
            continue
    else:
        if len(buffer) == 0 and int(a) == int(k):
            buffer.append(a)
        elif len(buffer) > 0 and a.isdigit():
            buffer.append(a)
        elif len(buffer) == 0 and int(a) != int(k):
            continue
if buffer:
    number = int(''.join(buffer))
    if number % 2 == 0:
        c+=1
        if c == 5:
            st = ""
            for i in str(number):
                st = st + dic.get(int(i)) + " "
            print(st)
            c = 0
        else:
            print(number)
print("Вот искомые числа")














