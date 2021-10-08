r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('инфаркт_миокарда.txt', 'w')

import re

for line in r.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.replace(' ИМ ', ' инфаркт миокарда ')
    text = text.replace(' Им ', ' инфаркт миокарда ')
    text = text.lower()
    text = text.replace(' инфаркт миокарда отрицает', ' ')
    text = text.replace(' инфаркт миокарда в анамнезе отрицает', ' ')
    text = text.replace(' инфаркт миокарда и онмк не переносил', ' ')
    text = text.replace('им в.а. алмазова', ' ')
    text = text.replace('им алмазова', ' ')
    text = text.replace('им павлова', ' ')
    text = text.replace('им и.и', ' ')
    text = text.replace('им джанелидзе', ' ')
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    res = '0'
    if (a[10] == 'АНАМНЕЗ_ЖИЗНИ') & (text.find('наследствен') != -1):
        continue
    if text.find(' инфаркт миокарда ') != -1:
        res = '1'
    if res != '0':
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()