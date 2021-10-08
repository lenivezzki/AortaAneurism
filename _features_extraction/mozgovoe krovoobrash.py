r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('мозговое_кровообращение.txt', 'w')

import re

for line in r.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'мозгово..? кровообра', 'ъъъ', text)
    text = re.sub(r'недостаточност. мозговое кровообра', 'ъъъ', text)
    text = re.sub(r'нарушен...?.? мозговое кровообра', 'ъъъ', text)
    text = re.sub(r'сосудисто-мозгов.. недостаточнос', 'ъъъ', text)
    text = re.sub(r'церебральн.. н', 'ъъъ', text)

    res = '0'
    if (a[10] == 'АНАМНЕЗ_ЖИЗНИ') & (text.find('наследствен') != -1):
        continue
    if text.find('ъъъ') != -1:
        res = '1'
    if res != '0':
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()