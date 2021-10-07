r = open('AortaAllPatients.txt', 'r')
w = open('AortaAllPatients_imt.txt', 'w')

#r = open('data.txt', 'r')
#w = open('rost_beta.txt', 'w')

import re


#индекс массы
def var1(text):
    res = re.findall(r' индекс массы тела \d\d?[.,]?\d?\d?', text)
    return res

def var2(text):
    res = re.findall(r' имт \d\d?[.,]?\d?\d?', text)
    return res

def isRestrict(res):
    if res != '':
        if float(res) > 50:
            return 1000
        else:
            if float(res) < 14:
                return -1000
            else:
                return 0
    else:
        return 10


for line in r.readlines():
    a = line.split('\t')
    text = a[11].lower()
    text = text.replace('293msl', ' ')
    text = text.replace('telom', ' имт ')
    text = text.replace('telos', ' ъъъ ')
    text = re.sub(r'id[a-z0-9]+ ', ' ', text)
    text = re.sub(r'[^а-я0-9., ]', ' ', text)
    text = re.sub(r' +', ' ', text)
    res1 = ''
    res2 = ''
    if text.find(' индекс массы тела') != -1:
        res1 = var1(text)
        if len(res1) >= 1:
            res1 = res1[len(res1)-1]
            res1 = re.sub(r'[^0-9.,]', '', res1)
            res1 = res1.replace(',', '.')
            #print(res1)
        else:
            res1 = ''
    if (text.find(' имт ') != -1) & (a[10] != 'ДАННЫЕ_КЛИНИЧЕСКОГО_ОБСЛЕДОВАНИЯ_(УВТ)'):
        res2 = var2(text)
        if len(res2) >= 1:
            res2 = res2[len(res2)-1]
            res2 = re.sub(r'[^0-9.,]', '', res2)
            res2 = res2.replace(',', '.')
        else:
            res2 = ''
    res = ''
    if res2 != '':
        res = res2
    if res1 != '':
        res = res1
#    if isRestrict(res) == 1000:
#        print(a[1])
#    if isRestrict(res) == -1000:
#        print(a[1])
    w.write(a[0] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()