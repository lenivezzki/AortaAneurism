import pymorphy2
import re

morph = pymorphy2.MorphAnalyzer()


r = open("tomsk_almazov ЛКА предложение_без_повтора.txt", "r")
w = open("tomsk_almazov ЛКА_LEMME.txt", "w")

for line in r.readlines():
    a = line.split('\t')
    text = a[1][:-1]
    text = text.lower()
    text = re.sub(r'[^а-я0-9% ё]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    words = text.split(' ')
    new_text = ''
    for word in words:
        p = morph.parse(word)[0]
        new_text = new_text + p.normal_form + ' '
    w.write(a[0] + '\t'+new_text+'\n')

r.close()
w.close()