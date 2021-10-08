f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('атеросклероз_аорты.txt', 'w')    #Глубокая гипотермия 14.1-20 ℃

import re

def var1(text):
    return re.findall(r'атеросклероз.? аорт', text)


for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'[^а-я ё]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = re.sub(r' +', ' ', text)
    res = '0'

    res1=var1(text)
    if len(res1) > 0:
        res='1'

    if res != '0':
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()