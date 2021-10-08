r = open('tomsk_almazov only_id_text.txt', 'r')
w = open('tomsk_almazov ЛКА.txt', 'w')


import re


prev_text = ''

for line in r.readlines():
    a = line.split('\t')
    text = ' ' + a[1][:-1] + ' '+'\n'
    text = text.lower()
    text = text.replace(' до ', ' ')
    text = text.replace(' ю ', ' ')
    text = text.replace('стенозы ', 'стеноз ')
    text = text.replace('стеноза ', 'стеноз ')
    text = text.replace('стенозов ', 'стеноз ')
    text = text.replace('окклюзии', 'окклюзия')
    text = text.replace('субокклюзии', 'окклюзия')
    text = text.replace('субокклюзия', 'окклюзия')
    text = text.replace('стенозированием', 'стеноз')
    text = text.replace('стенозированием', 'стеноз')
    text = text.replace('стенозирования', 'стеноз')
    text = text.replace('лкаствол', 'лка')
    text = text.replace('ствол лка', 'лка')
    text = text.replace('лка ствол', 'лка')
    text = text.replace('лка ствол', 'лка')
    text = re.sub(r' +', ' ', text)
    #text = text.replace('без формирования гемодинамически значимых стенозов', '')
    #text = text.replace('без гемодинамически значимого стеноз', '')
    #text = text.replace('без гемодинамически значимого стенозирования', '')
    #text = text.replace('без значимого стеноз', '')
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'лев.. коронарн.. артер..', 'лка', text)
    if a[0]=='GACAGqZAADAAA13:14AoAD':
        print('')
    if len(a[0]) < 4:
        text = text.replace(' ка ', ' лка ')
    text = re.sub(r' +', ' ', text)

    sentenses = text.split('.')
    for s in sentenses:
        if s.find(' лка') != -1:
            w.write(a[0]+'\t'+s+'\n')

r.close()
w.close()