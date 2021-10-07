r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('возраст_VER3.txt', 'w')

#r = open('data.txt', 'r')
#w = open('rost_beta.txt', 'w')

import re


def var1(text):
    res = re.findall(r' возраст ?\d\d?\d?', text)
    return res

#def var2(text):
#    res = re.findall(r'\d\d?\d? ?лет ', text)
#    return res

def var3(text):
    res = re.findall(r' возраст ?\d\d?\d? ?год', text)
    return res


def isRestrict(res):
    if res != '':
        if int(res) > 110:
            return 1000
        else:
            if int(res) < 10:
                return -1000
            else:
                return 0
    else:
        return 10


for line in r.readlines():
    a = line.split('\t')
    text = a[11].lower()
    text = text.replace('293age', 'возраст')
    text = re.sub(r'id[a-z0-9]+ ', ' ', text)
    text = re.sub(r'[^а-я0-9 ]', ' ', text)
    text = re.sub(r' +', ' ', text)
    res = ''
    if a[10] == 'EUROSCORE_RISK_PROFILE_РЕЗУЛЬТАТ':
        text = re.sub(r'.\d\d\d\d\d\d\d?', ' ', text)
        text = re.sub(r' +', ' ', text)
    if text.find('наследственность') != -1:
        continue
    res1 = var1(text)
#    res2 = var2(text)
    res3 = var3(text)
    if len(res1) > 0:
        res = res1[0]
        res = re.sub(r'[^0-9]', '', res)
#    if len(res2) > 0:
#        res = res2[0]
#        res = re.sub(r'[^0-9]', '', res)
    if len(res3) > 0:
        res = res3[0]
        res = re.sub(r'[^0-9]', '', res)
    if (isRestrict(res) == 1000) | (isRestrict(res) == -1000):
        res = ''
    if res != '':
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()