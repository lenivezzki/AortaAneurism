r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('впс.txt', 'w')

#r = open('data.txt', 'r')
#w = open('rost_beta.txt', 'w')

import re


for line in r.readlines():
    a = line.split('\t')
    text = a[11].lower()
    text = re.sub(r'[^а-я0-9ё ]', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = re.sub(r' врожденный порок', ' впс', text)
    res = '0'
    if text.find(' впс ') != -1:
        if a[10] != 'ЖАЛОБЫ':
            res = '1'
        if (a[10] == 'АНАМНЕЗ_ЗАБОЛЕВАНИЯ') & (text.find('наследственн') != -1):
            res = '0'
    if res != '0':
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()