f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('проксимальная_фенестрация.txt', 'w')    #Глубокая гипотермия 14.1-20 ℃

import re


for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'[^а-я0-9a-z ё.,]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = text.replace(' до ', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('гипотермия.', 'гипотермия')
    res = '0'
    #if (text.find('фенестрац') == -1) | (text.find('диссекци') == -1) | (text.find('расслоен') ==-1):
    #    #w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')
    #    continue
    sentenses = text.split('.')
    if a[1] == 'GACAFRq':
        print()
    for s in sentenses:
        if (s.find('фенестрац') != -1) | (s.find('диссекци') != -1) | (s.find('рассл')!=-1)|(s.find('debakey')!=-1):
            phrase = s.split(',')
            for p in phrase:
                if p.find('фенестрац') != -1:
                    p = ' '+p+' '
                    res = '5'
                    if (p.find(' дуг') != -1)|(p.find(' бца ') != -1)|(p.find(' бцс ') != -1):#дуга аорты
                        res += '3!'
                    if (p.find(' восх') != -1):#восходящий отдел
                        res += '2!'
                    if (p.find('синутобул') != -1)|(p.find(' стс ') != -1)|((p.find('корен') != -1))|((p.find('корн') != -1)):#синтобулярное соединение
                        res += '1!'
                if (p.find('рассл')!=-1) | (p.find('диссекци') != -1)|(p.find('debakey')!=-1):
                    if (p.find(' 3 тип') != -1)|(p.find('iii') != -1):  # за лпк
                        res += '4'
                    if (p.find(' ii ') != -1) | (p.find('2 тип') != -1):  # восходящий отдел
                        res += '2'
                    if (p.find(' дуг') != -1) & ((p.find(' ii ') != -1) | (p.find('2 тип') != -1)):  # дуга
                        res += '3'
                    if (p.find(' i ') != -1) | (p.find('1 тип') != -1):  # восход
                        res += '2'
    if len(res)>1:
        res = res[1:]
    if res != '0':
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()