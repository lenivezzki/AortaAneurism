r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('стеноз_вса_справа.txt', 'w')

import re

def var1(text):
    return re.findall(r'стеноз вса справа \d\d?', text)
def var2(text):
    return re.findall(r'стеноз справа вса \d\d?', text)
def var3(text):
    return re.findall(r'стеноз \d+ справа вса', text)


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
    if a[2] == 'GACAMsеABMAAA12:16AcAM':
        print(' ')
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('стенозы ', 'стеноз ')
    text = text.replace('стеноза ', 'стеноз ')
    text = text.replace('стенозие ', 'стеноз ')
    text = text.replace('стенозов ', 'стеноз ')
    text = text.replace('стенозом ', 'стеноз ')
    text = text.replace('стенозирование ', 'стеноз ')
    text = text.replace('рестеноз ', 'стеноз ')
    text = text.replace('субокклюзия', 'окклюзия')
    text = text.replace('субокклюзия', 'окклюзия')
    text = text.replace('субокклюзии', 'окклюзия')
    text = text.replace('оккулюзия', 'окклюзия')
    text = text.replace('окклюзии', 'окклюзия')
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'оса \d+ лвса \d+', '', text)
    text = re.sub(r'оса на протяжении верхней 3 до \d+ бифуркации до \d+', '', text)
    text = re.sub(r'бифуркации оса справа \d+', '', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('в пределах', '')
    text = text.replace('до', '')
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'поса \d+', '', text)
    text = text.replace('в ср 3', '')
    text = text.replace('с обеих сторон', 'справа')
    text = text.replace('с двух сторон', 'справа')
    text = text.replace('с 2 х сторон', 'справа')
    text = text.replace('стеноз обеих', 'стеноз справа')
    text = text.replace('бифуркации оса и', '')
    text = text.replace('бифуркаций оса и', '')
    text = text.replace('бифуркаций оса', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('в устье', '')
    text = text.replace('с двух сторон', 'справа')
    text = text.replace('бифуркаций оса и  ', '')
    text = text.replace('с обеих сторон', 'справа')
    text = text.replace('правого проксимального сегмента ', '')
    text = text.replace('в проксимальной трети ', '')
    text = text.replace('в пр 3 ', '')
    text = text.replace(' оса и', '')
    text = text.replace('от устья ', '')
    text = text.replace('в устьях ', '')
    text = text.replace('в средней трети ', '')
    text = text.replace('в средней части ', '')
    text = text.replace('в проксимальном отделе ', '')
    text = text.replace('на границы проксимальной и средней трети ', '')
    text = text.replace('на границе средней и дистальной трети ', '')
    text = text.replace('ср.трети ', '')
    text = text.replace('обеих вса', 'справа вса')
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'лвса \d+ ?\d?\d?', '', text)
    text = re.sub(r'оса \d+ ?\d?\d?', '', text)

    text = re.sub(r' +', ' ', text)

    text = text.replace('правой', 'справа')
    text = text.replace('левой', 'слева')
    text = text.replace('вса слева ', '')
    text = text.replace('вса слева ', '')
    text = text.replace('пвса', 'справа вса')
    text = text.replace('п вса', 'справа вса')
    text = text.replace('вса стеноз', 'стеноз вса')
    res = '0'


    #if a[1] == 'GACAMKY':
    #    print(' ')

    if (a[10] == 'АНАМНЕЗ_ЖИЗНИ') & (text.find('наследствен') != -1):
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')
        continue
    if text.find('вса') != -1:
        res1 = var1(text)
        res2 = var2(text)
        res3 = var3(text)
        if len(res3) >= 1:
            res = re.sub(r'[^0-9]+', '', res3[0])
        if len(res1) >= 1:
            res = re.sub(r'[^0-9]+', '', res1[0])
        if len(res2) >= 1:
            res = re.sub(r'[^0-9]+', '', res2[0])
        res = categoria(res)

    if(text.find('окклюзия справа стеноз вса') != -1):
        res = '4'

    w.write(a[1] + '\t'+ a[3]+'\t' + a[10] + '\t' + res + '\n')
print(k)
r.close()
w.close()