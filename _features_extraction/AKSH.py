f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('АКШ.txt', 'w')

import re

def var1(text):
    return re.findall(r'выполнена операция акш', text) #1

def var2(text):
    return re.findall(r'аутовенозное акш', text) #1


for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '

    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('рекомендовано проведение акш', '')
    text = text.replace('вмешательства акш', 'аутовенозное акш')
    text = text.replace('операции акш', 'аутовенозное акш')
    text = text.replace('после выполнения акш', 'выполнена операция акш')
    text = text.replace('после акш', 'выполнена операция акш')
    text = re.sub(r'аортокоронарн.. шунти', 'выполнена операция акш ', text)
    #text = text.replace('', 'выполнена операция акш')
    text = re.sub(r' +', ' ', text)

    res='0'

    if (a[10].find('ПРОТОКОЛ_ОПЕРАЦИИ') != -1) & (text.find(' акш') != -1):
        res ='1'
    if (a[10].find('АНАМНЕЗ_ЗАБОЛЕВАНИЯ') != -1) & (text.find(' акш') != -1):
        res ='1'
    if (a[10].find('ПРЕДСТАВЛЕНИЕ_О_БОЛЬНОМ') != -1) & (text.find(' акш') != -1):
        res ='1'
    if text.find(' акш') != -1:
        res = '1'

    res1 = var1(text)
    if len(res1) > 0:
        res = '1'

    res2 = var2(text)
    if len(res2) > 0:
        res = '1'


    w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()