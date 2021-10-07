r = open('patients_with operations_dataset.txt', 'r')
w = open('площадь_поверхности_тела.txt', 'w')

import re

def var1(text):
    return re.findall(r'площадь поверхности тела \d[.,]\d\d?', text)

def isRestricted(result):
    if float(result) > 2.8:
        return 0
    else:
        if float(result) <= 1.0:
            return 1
        else:
            return 2

for line in r.readlines():
    a = line.split('\t')
    text = ' ' + a[10] + ' '
    text = text.lower()
    text = text.replace('293msltelos', 'площадь поверхности тела')
    text = text.replace(' bsa ', ' площадь поверхности тела ')
    text = text.replace('b ППТ /b', ' площадь поверхности тела ')
    text = re.sub(r'[^а-я0-9,. ё]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    res = ''

    if text.find('площадь поверхности тела') != -1:
        res1 = var1(text)
        if len(res1) >= 1:
            res = re.sub(r'[^0-9,.]+', '', res1[0])
            res = res.replace(',', '.')
            #test = isRestricted(res)
            #if test == 0:
            #    print(a[1])
            #if test == 1:
            #    print(a[1])

    w.write(a[0] + '\t' + a[9] + '\t' + res + '\n')

r.close()
w.close()