k = input()
f = open('txt1.txt', 'r')
buffer = []
c = 0
dic = {1:'один',2:'два',3:'три',4:'четыре',5:'пять',6:'шесть',7:'семь',8:'восемь',9:'девять'}
s = f.read()
for a in s:
    if len(buffer) == 0 and a == k:
        buffer.append(a)
    elif len(buffer) > 0 and a.isdigit():
        buffer.append(a)
    elif len(buffer) == 0 and a != k:
        continue
    else:
        number = int(''.join(buffer))
        if number % 2 == 0:
            c+=1
            if c == 5:
                for i in str(number):
                    print(dic.get(int(i)))
            else:
                print(number)
        buffer.clear()














