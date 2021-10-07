f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('гематокрит.txt', 'w')

import re

def var1(text):
    return re.findall(r'гематокрит ?\d+[.,]?\d+?', text) #гематокрит 0,131

def var2(text):
    return re.findall(r'гематокритт ?\d+[.,]\d', text) #HCT гематокрит 37.040.0-48.0 (40-48 показатели нормы, лишнее)

def var3(text):
    return re.findall(r'эритроциты ?\d+[.,]?\d+?', text)  # гематокрит 0,131



def mm_to_l(res):
    res = res.replace(',', '.')
    if res.find('х') == -1:
        try:
            res = str(float(res) / 100.0)
        except ValueError:
            print(res)
    else:
        res = res.replace('.', '')
    return res

def m_to_l(res):
    res = res.replace(',', '.')
    if res.find('х') == -1:
        try:
            res = str(float(res) / 10.0)
        except ValueError:
            print(res)
    else:
        res = res.replace('.', '')
    return res

def check(res):
    if res != '':
        try:
            if (float(res) > 1.0) | (float(res) < 0.05):
                return 0
        except ValueError:
            print('ferror')
    return 1

for line in f.readlines():
    a = line.split('\t')
    if a[10].find('РЕКОМЕНДАЦИ') != -1:
        continue
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = text.replace('hct', 'гематокритт')
    text = text.replace(' ht ', 'гематокрит')
    text = text.replace('составляет ', '')
    text = text.replace('до', '')

    text = text.replace('дата', '')
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace(' средний объем эритроцитов', '')
    text = text.replace(' эритроцитов', ' эритроциты')

    res=''

    #эритроциты 3,08
    res3 = var3(text)
    if len(res3) > 0:
        res = re.sub(r'[^0-9.,]+', '', res3[len(res2) - 1])
        res = m_to_l(res)

    #гематокрит 0,131
    res1 = var1(text)
    if len(res1) > 0:
        res = re.sub(r'[^0-9.,]+', '', res1[len(res1) - 1])
        res = res.replace(',', '.')
        if float(res) >= 1:
            res = mm_to_l(res)

    # HCT гематокрит 37.040.0-48.0 (40-48 показатели нормы, лишнее)
    res2 = var2(text)
    if len(res2) > 0:
        res = re.sub(r'[^0-9.,]+', '', res2[len(res2) - 1])
        res = mm_to_l(res)




    if check(res) == 0:
        if res[:2] == '61':
            res = res[2:]
        else:
            res=''

    if res != '':
        w.write(a [1] + '\t' + a [3] + '\t' + a [10] + '\t' + res + '\n')

f.close()
w.close()