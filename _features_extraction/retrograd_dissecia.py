f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('ретроградная_диссекция.txt', 'w')    #Глубокая гипотермия 14.1-20 ℃

import re


def var1(text):
    return re.findall(r' протяженность расслоения \d+[.,]?\d+?', text) #гипотермии(я) 27

for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '

    text = re.sub(r'[^а-я0-9 ё.,]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = text.replace('расслоившейся стенки', 'расслоения')
    text = text.replace('составляет около', '')
    text = text.replace(' до ', '')
    text = re.sub(r' +', ' ', text)
    res = '0'
    if text.find('диссекц') == -1:
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')
        continue
    sentenses = text.split('.')
    for s in sentenses:
        if s.find('диссекц') != -1:
            phrase = s.split(',')
            for p in phrase:
                if p.find('диссекц') != -1:
                    p = ' '+p+' '
                    if (p.find('проксима') != -1)|(p.find(' ретроград') != -1):#синтобулярное соединение
                        res = '1'


    w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()