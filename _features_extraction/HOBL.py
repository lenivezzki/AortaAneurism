r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('ХОБЛ.txt', 'w')

import re

for line in r.readlines():
    a = line.split('\t')
    text = a[11] + ' '
    text = text.lower()
    text = text.replace('хроническая обструктивная болезнь легких', ' хобл ')
    text = text.replace('хронической обструктивной болезнью легких', ' хобл ')
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    res = '0'
    if (a[10] == 'АНАМНЕЗ_ЖИЗНИ') & (text.find('наследствен') != -1):
        continue
    if text.find(' хобл ') != -1:
        res = '1'
    if res != '0':
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()