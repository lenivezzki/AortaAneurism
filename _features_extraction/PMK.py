f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('ПМК.txt', 'w')

import re

def var1(text):
    return re.findall(r'выполнена операция пмк ', text) #1

def var2(text):
    return re.findall(r'аутовенозное пмк', text) #1


for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '

    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('рекомендовано проведение пмк ', '')
    text = text.replace('мелодия пмк ', '')
    text = text.replace('град на пмк ', '')
    #text = text.replace(' пак без признаков дисфу', '')
    text = text.replace('перед оперативным лечением пмк ', '')
    text = text.replace(' нет пмк ', ' ')
    #text = text.replace('нормалньо функционирующий пак', ' ')
    text = text.replace('вмешательства пмк ', 'выполнена операция пмк ')
    text = text.replace('операции пмк ', 'выполнена операция пмк ')
    text = text.replace('после выполнения пмк ', 'выполнена операция пмк ')
    text = text.replace('после пмк ', 'выполнена операция пмк ')
    text = re.sub(r'протезирован.. митр', 'выполнена операция пмк ', text)
    #text = text.replace('', 'выполнена операция акш')
    text = re.sub(r' +', ' ', text)

    res='0'

    if (a[10].find('ПРОТОКОЛ_ОПЕРАЦИИ') != -1) & (text.find(' пмк ') != -1):
        res ='1'
    if (a[10].find('АНАМНЕЗ_ЗАБОЛЕВАНИЯ') != -1) & (text.find(' пмк ') != -1):
        res ='1'
    if (a[10].find('ПРЕДСТАВЛЕНИЕ_О_БОЛЬНОМ') != -1) & (text.find(' пмк ') != -1):
        res ='1'
    if (a[10].find('ОСМОТР_ХИРУРГА') != -1) & (text.find(' пмк ') != -1):
        res ='1'
    if (a[10].find('ПРЕДОПЕРАЦИОННЫЙ_ЭПИКРИЗ') != -1) & (text.find(' пмк ') != -1):
        res ='1'
    if (a[10].find('ДНЕВНИК_НАБЛЮДЕНИЙ') != -1) & (text.find(' пмк ') != -1):
        res ='1'
    if text.find(' пмк ') != -1:
        res = '1'

    res1 = var1(text)
    if len(res1) > 0:
        res = '1'


    if (a[10].find('ПОЯСНЕНИЯ_К_НАЗНАЧЕНИЮ') != -1) & (text.find(' пмк ') != -1):
        res ='0'
    if (a[10].find('ДНЕВНИК') != -1) & (text.find(' пмк ') != -1):
        res ='0'

    w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()