f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('стеноз_мк.txt', 'w')    #Глубокая гипотермия 14.1-20 ℃

import re


def var1(text):
    return re.findall(r' недостаточность мк ', text) #гипотермии(я) 27

for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'[^а-я0-3i ё.,]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = text.replace(' до ', '')
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'митральн...? клапана?', 'мк ', text)
    text = re.sub(r'митральн...?', 'мк ', text)
    text = text.replace('стенозы ', 'стеноз ')
    text = text.replace('стеноза ', 'стеноз ')
    text = text.replace('мк стенозирование', 'стеноз мк')
    text = text.replace('мк стенозирована', 'стеноз мк')
    text = text.replace('субокклюзия', 'окклюзия')
    text = text.replace('субокклюзия', 'окклюзия')
    text = text.replace('субокклюзии', 'окклюзия')
    text = text.replace('окклюзии', 'окклюзия')
    text = text.replace('окклюзия', 'стеноз')
    text = re.sub(r' +', ' ', text)
    text = text.replace('правого проксимального сегмента ', '')
    text = text.replace('в проксимальной трети ', '')
    text = text.replace('в пр 3 ', '')
    text = text.replace('от устья ', '')
    text = text.replace('в средней трети ', '')
    text = text.replace('в средней части ', '')
    text = text.replace('в проксимальном отделе ', '')
    text = text.replace('на границы проксимальной и средней трети ', '')
    text = text.replace('на границе средней и дистальной трети ', '')
    text = text.replace('пка стеноз п ', 'пка стеноз ')
    text = text.replace('ср.трети ', '')
    text = text.replace('мк стеноз', 'стеноз мк')

    res = '0'
    if text.find(' мк ') == -1:
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')
        continue

    sentenses = text.split('.')
    for s in sentenses:
        s = ' '+s+' '
        if s.find(' мк ') != -1:
            phrase = s.split(',')

            for p in phrase:
                p = ' ' + p + ' '
                if (p.find(' мк ') != -1) & (p.find(' стеноз') != -1):
                    res = '4'
                    if (p.find(' легк') != -1) | (p.find(' 1 ст') != -1) | (p.find(' i ') != -1)|\
                            (p.find(' провод') != -1):
                        res = '1'
                    if (p.find(' умерен') != -1) | (p.find(' 2 ст') != -1) | (p.find(' ii ') != -1)|\
                            (p.find(' значим') != -1):
                        res = '2'
                    if (p.find(' выражен') != -1) | (p.find(' 3 ст') != -1) | (p.find(' iii') != -1)|\
                            (p.find(' тяжел') != -1):
                        res = '3'

    w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()