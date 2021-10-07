r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('стеноз_пна.txt', 'w')

import re

def var1(text):
    return re.findall(r' пна \d\d?', text)
def var2(text):
    return re.findall(r' пна до \d\d?', text)


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
    text = re.sub(r'передн.. нисходящ.. артер..', 'пна', text)
    text = text.replace('в проксимальном сегменте', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('субокклюзия', 'окклюзия')
    text = text.replace('субокклюзии', 'окклюзия')
    text = text.replace('окклюзии', 'окклюзия')
    text = re.sub(r' +', ' ', text)
    text = text.replace(' окклюзия пна', ' пна окклюзия')
    res = '0'

    if (a[9] == 'АНАМНЕЗ_ЖИЗНИ') & (text.find('наследствен') != -1):
        continue
    if a[2] == 'GACAXкGAAZAAB20:19AsAJ':
        print(a[1])
    if text.find(' пна ') != -1:
        k = k + 1
        res1 = var1(text)
        res2 = var2(text)
        if len(res1) >= 1:
            res = re.sub(r'[^0-9]+', '', res1[0])
        if len(res2) >= 1:
            res = re.sub(r'[^0-9]+', '', res2[0])
        if res != '':
            res = categoria(res)
        else:
            res = '0'
    if (text.find('пна окклюзия') != -1):
        k = k + 1
        res = '4'
    if res != '0':
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')
print(k)
r.close()
w.close()