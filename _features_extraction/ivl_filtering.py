"""
r = open('ивл.txt', 'r')

import re


ivl = ['дыхание вспомогательная вентиляция легких',
       'дыхание ввл',
       'дыхание неинвазивная вентиляция легких',
       'дыхание ивл',
       'дыхание через тст',
       'дыхание через трахеостомическую трубку',
       'дыхание режим ивл ввл',
       'дыхание вентиляция',
       'дыхание переведен на ввл',
       'дыхание проводятся сеансы нивл',
       'дыхание на фоне проведения нивл',
       'дыхание через трахеостому'
       ]

sam = ['дыхание самостоятельное',
       'дыхание спонтанное'
       ]

dict = {}

for line in r.readlines():
    a = line.split('\t')
    text = ' ' + a[4] + ' .'
    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = re.sub(r' +', ' ', text)
    ivl_i = '-1'
    for i in ivl:
        if text.find(i) != -1:
            ivl_i = '1'
            break
    for s in sam:
        if text.find(s) != -1:
            ivl_i = '0'
    if a[0] not in dict:
        dict[a[0]] = {a[1]+'\t'+a[2]: ivl_i}
    else:
        dict [a [0]] [a [1] + ' ' + a [2]] = ivl_i

r.close()

w = open('ивл_сутки.txt', 'w')

for d_keys in dict.keys():
    for data_keys in dict[d_keys].keys():
        w.write(d_keys + '\t' + data_keys + '\t' + dict[d_keys][data_keys]+'\n')
w.close()

"""

r = open('oper_postoper_period.txt', 'r')

list_oper = []
for line in r.readlines():
    list_oper.append(line[:-1])
r.close()

r = open('ивл_сутки.txt', 'r')
dict = {}

for line in r.readlines():
    a = line.split('\t')
    char = int(a[3][:-1])
    if a[0] not in dict:
        dict[a[0]] = {a[1]: char}
    else:
        if a[1] not in dict[a[0]]:
            dict[a[0]][a[1]] = char
        else:
            dict[a[0]][a[1]] += char

r.close()
w = open('ивл_метки.txt', 'w')

for i in range(0,len(list_oper)):
    a = list_oper[i].split('\t')
    if a[0] == 'GACAO1Й':
        print()
    start = int(a[1])
    end = int(a[2])
    days = 0
    flag = False
    for patient in dict:
        if flag:
            break
        if patient != a[0]:
            continue
        if patient == 'GACAO1Й':
            print()
        for date in dict[patient]:
             if (int(date) <= end+10) & (int(date) >= start-10):
                if dict[patient][date] > 0:
                    days += 1
                flag = True
    res = '0'
    if days > 7:
        res = '1'
    w.write(list_oper[i] + '\t'+ res +'\n')
w.close()

