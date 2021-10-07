r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('артериальная_гипертензия.txt', 'w')

import re

for line in r.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = text.replace(' аг отрицает', ' ')
    text = text.replace(' аг никогда не', ' ')
    text = text.replace(' нил аг ', ' ')
    text = text.replace(' кт аг ', ' ')
    text = text.replace(' мскт аг ', ' ')
    text = text.replace('АГ/АТ', ' ')
    text = re.sub(r' артериальн..? гипертанз..? ', ' аг ', text)
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    res = '0'
    if (a[10] == 'АНАМНЕЗ_ЖИЗНИ') & (text.find('наследствен') != -1):
        continue
    if text.find(' аг ') != -1:
        res = '1'
    if res != '0':
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()