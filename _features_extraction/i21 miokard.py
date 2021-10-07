f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('i21_инфаркт_миокарда.txt', 'w')

import re

for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'[,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('острый инфаркт', 'i21')

    res = '0'

    if text.find('i21') != -1:
        res = '1'

    w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()