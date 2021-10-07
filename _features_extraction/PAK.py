f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('ПАК.txt', 'w')

import re

def var1(text):
    return re.findall(r'выполнена операция пак ', text) #1

def var2(text):
    return re.findall(r'аутовенозное акш', text) #1


for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '

    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('рекомендовано проведение пак ', '')
    text = text.replace('мелодия пак ', '')
    text = text.replace('град на пак ', '')
    #text = text.replace(' пак без признаков дисфу', '')
    text = text.replace('перед оперативным лечением пак ', '')
    text = text.replace(' нет пак ', ' ')
    #text = text.replace('нормалньо функционирующий пак', ' ')
    text = text.replace('вмешательства пак ', 'выполнена операция пак ')
    text = text.replace('операции пак ', 'выполнена операция пакк ')
    text = text.replace('после выполнения пак ', 'выполнена операция пак ')
    text = text.replace('после пак ', 'выполнена операция пак ')
    text = re.sub(r'протезирован.. аортальн...?', 'выполнена операция пак ', text)
    #text = text.replace('', 'выполнена операция акш')
    text = re.sub(r' +', ' ', text)

    res='0'

    if (a[10].find('ПРОТОКОЛ_ОПЕРАЦИИ') != -1) & (text.find(' пак ') != -1):
        res ='1'
    if (a[10].find('АНАМНЕЗ_ЗАБОЛЕВАНИЯ') != -1) & (text.find(' пак ') != -1):
        res ='1'
    if (a[10].find('ПРЕДСТАВЛЕНИЕ_О_БОЛЬНОМ') != -1) & (text.find(' пак ') != -1):
        res ='1'
    if text.find(' пак ') != -1:
        res = '1'

    res1 = var1(text)
    if len(res1) > 0:
        res = '1'


    if (a[10].find('ПОЯСНЕНИЯ_К_НАЗНАЧЕНИЮ') != -1) & (text.find(' пак ') != -1):
        res ='0'
    if (a[10].find('ДНЕВНИК') != -1) & (text.find(' пак ') != -1):
        res ='0'

    w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()