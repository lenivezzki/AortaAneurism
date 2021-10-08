f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('гемоглобин.txt', 'w')

import re

def var1(text):
    return re.findall(r'гемоглобин ?\d+ ?г? ?л?', text)

def var2(text):
    return re.findall(r'гемоглобин ?\d+[.,]\d+', text)

def var3(text):
    return re.findall(r'гемоглобин г л 1\d0\.0 1\d0\.0 \d+[.,]\d+', text)

def var3(text):
    return re.findall(r'гемоглобин в динамике \d?\d\.\d\d\.\d\d\d?\d? ?г?\.? \d+ г л \d+ г л', text)

def check(res):
    if res != '':
        try:
            if (float(res) > 300.0) | (float(res) < 20.0):
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
    text = text.replace('hgb', 'гемоглобин')
    text = text.replace(' hba ', 'гемоглобин')
    text = text.replace(' hb ', ' гемоглобин ')
    text = re.sub(r'293pan\d', '', text)
    text = text.replace('hba1c', '')
    text = text.replace('g/l', 'г л')
    text = text.replace('g l', 'г л')
    text = text.replace('до', '')
    text = text.replace('дата', '')
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('гемоглобина','гемоглобин')
    text = text.replace('в крови без динамики ', '')
    text = text.replace('1 раз в 3 месяца', '')
    text = text.replace('1 раз в месяц', '')
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'гемоглобин \d?\d\.\d\d\.\d\d\d?\d? ?г?\.? от', 'гемоглобин', text)
    text = re.sub(r'гемоглобин \d?\d\.\d\d\.\d\d\d?\d?,?', 'гемоглобин', text)
    text = text.replace('при дооперационном уровне гемоглобин', '')
    text = text.replace('эритроциты гемоглобин', '')
    text = text.replace('среднее содержание гемоглобин', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('гликолизированный гемоглобин', '')
    text = text.replace('гликозилированный гемоглобин', '')
    text = text.replace('гликозилированного гемоглобин', '')
    text = text.replace('гликированный гемоглобин', '')
    text = text.replace('гликированного гемоглобин', '')
    text = text.replace('гликированого гемоглобин', '')
    text = text.replace('гликолизированного гемоглобин', '')
    text = text.replace('глик. гемоглобин', '')
    text = re.sub(r' +', ' ', text)

    res=''

    #гемоглобин 88 г л
    res1 = var1(text)
    if len(res1) > 0:
        res = re.sub(r'[^0-9]+', '', res1[len(res1) - 1])

    # гемоглобин 88,4
    res2 = var2(text)
    if len(res2) > 0:
        res = re.sub(r'[^0-9.,]+', '', res2[len(res2) - 1])
        res = res.replace(',', '.')

        # гемоглобин 88 г л
    res3 = var3(text)
    if len(res3) > 0:
        res = re.sub(r'[^0-9., ]+', '', res3[len(res3) - 1])
        r = res.split(' ')
        res = r[len(r)-1]


    if check(res) == 0:
        if res[:2] == '61':
            res = res[2:]
        else:
            res=''
    if res != '':
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()