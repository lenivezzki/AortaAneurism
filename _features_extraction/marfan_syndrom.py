r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('синдром_марфана.txt', 'w')

#r = open('data.txt', 'r')
#w = open('rost_beta.txt', 'w')

import re


for line in r.readlines():
    a = line.split('\t')
    text = a[11].lower()
    text = re.sub(r'[^а-я0-9ё ]', ' ', text)
    text = re.sub(r' +', ' ', text)
    res = '0'
    if text.find(' марфан') != -1:
        res = '1'
        if (a[10] == 'АНАМНЕЗ_ЖИЗНИ') & (text.find('наследственн') != -1):
            res = '0'
    if res != '0':
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()