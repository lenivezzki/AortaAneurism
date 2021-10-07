r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('стеноз_пка.txt', 'w')

import re

def var1(text):
    return re.findall(r'стеноз пка \d\d?', text)
def var2(text):
    return re.findall(r'стеноз пка до \d\d?', text)
def var3(text):
    return re.findall(r'\d+ стеноз пка', text)
def var4(text):
    return re.findall(r'стеноз пка в ср 3 \d\d?', text)

def categoria(res):
    if int(res) > 99:
        return '0'
    if int(res) >= 75:
        return '3'
    else:
        if int(res) >= 50:
            return '2'
        else:
            if int(res) != 0:
                return '1'
    return '0'

k = 0
for line in r.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('стенозы ', 'стеноз ')
    text = text.replace('стеноза ', 'стеноз ')
    text = text.replace('пка стенозирование', 'стеноз пка')
    text = text.replace('пка стенозирована', 'стеноз пка')
    text = text.replace('субокклюзия', 'окклюзия')
    text = text.replace('субокклюзия', 'окклюзия')
    text = text.replace('субокклюзии', 'окклюзия')
    text = text.replace('окклюзии', 'окклюзия')
    text = re.sub(r' +', ' ', text)
    text = text.replace('правого проксимального сегмента ', '')
    text = text.replace('в проксимальной трети ', '')
    text = text.replace('в пр 3 ', '')
    text = text.replace('от устья ', '')
    text = text.replace('в средней трети ', '')
    text = text.replace('в средней части ', '')
    text = text.replace('в проксимальном отделе ', '')
    text = text.replace('на границы проксимальной и средней трети ', '')
    text = text.replace('на границе средней и дистальной трети ', '')
    text = text.replace('пка стеноз п ', 'пка стеноз ')
    text = text.replace('ср.трети ', '')
    text = text.replace('пка окклюзия','окклюзия пка')
    text = text.replace('пка до окклюзия', 'окклюзия пка')
    text = re.sub(r' +', ' ', text)
    text = text.replace('пка стеноз', 'стеноз пка')
    res = '0'

    if (a[9] == 'АНАМНЕЗ_ЖИЗНИ') & (text.find('наследствен') != -1):
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')
        continue
    if text.find('стеноз пка ') != -1:
        k = k + 1
        res1 = var1(text)
        res2 = var2(text)
        res3 = var3(text)
        res4 = var4(text)
        if len(res3) >= 1:
            res = re.sub(r'[^0-9]+', '', res3[0])
        if len(res1) >= 1:
            res = re.sub(r'[^0-9]+', '', res1[0])
        if len(res2) >= 1:
            res = re.sub(r'[^0-9]+', '', res2[0])
        if len(res4) >= 1:
            res4[0] = res4[0].replace('3', '')
            res = re.sub(r'[^0-9]+', '', res4[0])
        res = categoria(res)
    if text.find('окклюзия пка') != -1:
        k = k + 1
        res = '4'

    w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')
print(k)
r.close()
w.close()