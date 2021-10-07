r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('госпитальная_летальность.txt', 'w')

import re


for line in r.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    res = '0'
    if (a[9] == 'ПОСМЕРТНЫЙ_ЭПИКРИЗ') | (a[9] == 'ПРОТОКОЛ_УСТАНОВЛЕНИЯ_СМЕРТИ_ЧЕЛОВЕКА'):
        res = '1'
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')
        continue
    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('брат умер', '')
    text = text.replace('отец смерть', '')
    text = text.replace('отец умер', '')
    text = text.replace('отец смерть', '')
    text = text.replace('мать умер', '')
    text = text.replace('мать смерть', '')
    text = text.replace('муж умер', '')
    text = text.replace('жена умер', '')
    text = text.replace(' смерть родственник', '')
    text = text.replace('умер в возрасте 9 мес со слов', '')
    text = text.replace('ст. умер ', '')
    text = re.sub(r' +', ' ', text)

    if (a[9] == 'АНАМНЕЗ_ЖИЗНИ') & (text.find('наследствен') != -1):
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')
        continue

    if (text.find('умер ') != -1):
        res = '1'
    if (text.find('биологическая смерть ') != -1):
        res = '1'
    if (text.find('диагноз смерти основной ') != -1):
        res = '1'
    if len(re.findall(r'смерть \d\d?.\d\d.\d\d', text)) > 0:
        res = '1'
    w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()