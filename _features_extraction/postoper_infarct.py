r = open('patients only_after operation.txt', 'r')
w = open('постопер_инфаркт.txt', 'w')

import re

#переносит им

for line in r.readlines():
    a = line.split('\t')
    text = a[11]
    text = text.lower()
    text = re.sub(r'[^а-я ё]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('постинфарктный им ', '')
    text = text.replace('пикс им ', '')
    text = text.replace('данных за им нет ', '')
    text = re.sub(r'им в \d\d\d\d','',text)
    text = re.sub(r'им \d\d\d\d', '', text)
    text = text.replace('вызван хирург им ',' ')
    if text.find(' им ') != -1:
        w.write(a[1]+'\t'+a[3]+'\t'+a[10]+'\t1\n')
r.close()
w.close()
