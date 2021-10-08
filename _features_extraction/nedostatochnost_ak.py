f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('недостаточность_ак.txt', 'w')    #Глубокая гипотермия 14.1-20 ℃

import re


def var1(text):
    return re.findall(r' недостаточность ак ', text) #гипотермии(я) 27

for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'[^а-я0-3i ё.,]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = text.replace(' до ', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace(' аок ', ' ак ')
    text = re.sub(r'аортальн...? клапана?', 'ак ', text)
    text = re.sub(r'аортальн...?', 'ак ', text)


    res = '0'
    if text.find(' ак ') == -1:
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')
        continue

    sentenses = text.split('.')
    for s in sentenses:
        if s.find(' ак ') != -1:
            phrase = s.split(',')
            for p in phrase:
                if (p.find(' ак ') != -1) & (p.find(' недоста') != -1):
                    res = '4'
                    if (p.find(' легк') != -1) | (p.find(' 1 ст') != -1) | (p.find(' i ') != -1):
                        res = '1'
                    if (p.find(' умерен') != -1) | (p.find(' 2 ст') != -1) | (p.find(' ii ') != -1):
                        res = '2'
                    if (p.find(' выражен') != -1) | (p.find(' 3 ст') != -1) | (p.find(' iii') != -1):
                        res = '3'

    w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()