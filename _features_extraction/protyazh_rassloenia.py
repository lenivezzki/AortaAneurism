f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('протяженность_расслоения.txt', 'w')    #Глубокая гипотермия 14.1-20 ℃

import re


def var1(text):
    return re.findall(r' протяженность расслоения \d+[.,]?\d+?', text) #гипотермии(я) 27

for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    #if (a[10].find('ПРОТОКОЛ_ОПЕРАЦИИ')!=-1) | (a[10] == 'ПРЕДОПЕРАЦИОННЫЙ_ЭПИКРИЗ') | (a[10].find('ДИАГНОЗ')!=-1):
    #    continue
    text = text.replace('ДИАГНОЗ_УТОЧНЕННЫЙ_ОСНОВНОЙ I71 Аневризма и расслоение аорты', ' ')
    text = text.lower()
    text = text.replace('признаками расслоения', '')
    text = re.sub(r'[^а-я0-9a-z ё.,]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = text.replace('убедительных данных за расслоение', '')
    text = text.replace('составляет около', '')
    text = text.replace('без признаков расслоения', '')
    text = text.replace(' до ', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('торако абдоминальн', 'торакоабдоминальн')
    text = text.replace('расслаивающ', 'расслоивающ')
    text = text.replace('признаков расслоения стенки не выявлено', '')
    text = text.replace('расслаивающая аневризма аорты, переходящ', 'расслаивающая аневризма аорты переходящ')
    text = text.replace('де бейки', 'дебейки')


    res = '0'
    sentenses = text.split('.')
    for s in sentenses:
        if (s.find('рассл')!=-1)|(s.find('debakey')!=-1)|(s.find('дебейки')!=-1):
            phrase = s.split(',')
            for p in phrase:
                if (p.find('рассл')!=-1)|(p.find('debakey')!=-1)|(p.find('дебейки')!=-1):
                    p = ' ' + p + ' '
                    p = re.sub(r'рассл.+не выявлено', ' ', p)
                    if (p.find('торакоабдоминальн') != -1)|(p.find('брюш') != -1):  # брюшной
                        res += '4'
                    if (p.find(' 3 тип') != -1)|((p.find('iii') != -1))|(p.find('1 тип') != -1)|\
                            (p.find(' i ') != -1):
                        res += '4!'
                    if (p.find(' нисх') != -1) | (p.find(' торакоабдоминальн') != -1):  # нисходящий
                        res += '3'
                    if (p.find(' 3 тип') != -1)|(p.find(' i ') != -1)|(p.find('iii') != -1)|\
                            (p.find('1 тип') != -1):
                        res += '3!'
                    if (p.find(' ii ') != -1) | (p.find('2 тип') != -1)|\
                            (p.find('1 тип') != -1) | (p.find(' i ') != -1):  # восходящий отдел
                        res += '1!'
                    if (p.find(' восх') != -1):
                        res += '1'
                    if (p.find(' ii ') != -1) | (p.find('2 тип') != -1):  # дуга
                        res += '2!'
                    if (p.find(' дуг') != -1):
                        res += '2'
                    if (p.find(' бедр') != -1) | (p.find('подздош') != -1) |\
                            (p.find(' почеч') != -1)|(p.find(' инфрар') != -1):  # бедрен подздош
                        res += '5'
    if len(res)>1:
        res = res[1:]
    if res != '0':
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()