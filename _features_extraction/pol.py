r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('pol.txt', 'w')


import re


def var1(text):
    res = re.findall(r' пол [жм]\s', text)
    return res

def var2(text):
    res = re.findall(r' пол женс?к?и?й?\s', text)
    return res

def var3(text):
    res = re.findall(r' пол мужс?к?о?й?\s', text)
    return res

def var4(text):
    res = re.findall(r' женщ?и?н?а? \d\d', text)
    return res

def var5(text):
    res = re.findall(r' мужч?и?н?а? \d\d', text)
    return res


def determine_sex(res):
    if res == '':
        return ''
    if res.find('м') != -1:
        return 'мужской'
    if res.find('ж') != -1:
        return 'женский'
    return ''

def cut(res):
    return re.sub(r'[^а-я]', '', res)

for line in r.readlines():
    a = line.split('\t')
    text = ' ' + a[11].lower() + ' '
    text = text.replace('Пациент/ка', 'пациент')
    text = re.sub(r'id[a-z0-9]+ ', ' ', text)
    text = re.sub(r'[^а-я0-9ё ]', ' ', text)
    text = re.sub(r' +', ' ', text)
    res = ''
    if text.find(' пол ') != -1:
        if a[10] == 'EUROSCORE_RISK_PROFILE_РЕЗУЛЬТАТ':
            text = re.sub(r'пол женский', 'пол', text)
            text = re.sub(r' +', ' ', text)
        res1 = var1(text)
        res2 = var2(text)
        res3 = var3(text)
        if len(res3) > 0:
            res = res3[0]
            res = cut(res)
            res = determine_sex(res)
        if len(res2) > 0:
            res = res2[0]
            res = cut(res)
            res = determine_sex(res)
        if len(res1) > 0:
            res = res1[0]
            res = cut(res)
            res = determine_sex(res)

    if res == '':
        res1 = var4(text)
        res2 = var5(text)
        if len(res1) > 0:
            res = res1[0]
            res = cut(res)
            res = determine_sex(res)
        if len(res2) > 0:
            res = res2[0]
            res = cut(res)
            res = determine_sex(res)



    if res == '':
        #res1 = re.findall(r'пациент[ауое]', text)
        #if len(res1) > 0:
        #    res = 'мужской'

        res1 = re.findall(r'пациентк', text)
        if len(res1) > 0:
            res = 'женский'

    if res=='женский':
        res='0'
    if res == 'мужской':
        res='1'
    if res != '':
        w.write(a[1] +'\t'+a[3] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()