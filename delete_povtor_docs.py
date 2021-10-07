r = open('tomsk_almazov ЛКА.txt', 'r')
w = open('tomsk_almazov ЛКА предложение_без_повтора.txt', 'w')

dict_clean = {}
arr_clean = []

import re

for line in r.readlines():
    a = line.split('\t')
    text = a[4]
    id = a[0]
    text = text.lower()
    text = re.sub(r'[^а-яё]+', '', text)
    sort_text = id+''.join(sorted(text))
    if sort_text not in arr_clean:
        arr_clean.append(sort_text)
        w.write(line)


r.close()
w.close()
