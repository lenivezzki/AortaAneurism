k = open('patients_with operations_dataset_clean.txt', 'r')
w = open('фракции_выброса.txt', 'w')

import re

def var1(text):
    return re.findall(r'фв симпсон \d+', text)

def var2(text):
    return re.findall(r'фв тейхольц \d+', text)

def var3(text):
    return re.findall(r' фв лж \d+', text)

def var4(text):
    return re.findall(r' снижение фв до \d+', text)

def var5(text):
    return re.findall(r' фв ?\d+', text)


def smallest(mas):
    min = 101
    for i in range(0,len(mas)):
        num = int(re.sub(r'[^0-9]+', '', mas[i]))
        if num < min:
            min = num
    return str(min)

def check(res):
    if res != '':
        if int(res) > 100:
            return 0
    return 1

for line in k.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = text.replace('293eks_frak', '')
    text = text.replace('293ikd_frak', '')
    text = text.replace('simpson', 'симпсон')
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('по симпсон', 'симпсон')
    text = text.replace('фракция выброса', 'фв')
    text = text.replace('фракции выброса', 'фв')
    text = text.replace('левого желудочка', 'лж')
    text = re.sub(r' +', ' ', text)


    res = ''
    if text.find('фв') != -1:
        r = var1(text)
        if len(r) > 0:
            res = smallest(r)

        r = var2(text)
        if len(r) > 0:
            res = smallest(r)

        r = var3(text)
        if len(r) > 0:
            res = smallest(r)

        r = var4(text)
        if len(r) > 0:
            res = smallest(r)

        r = var5(text)
        if len(r) > 0:
            res = smallest(r)

    if check(res) == 0:
        if r[0].find('61') == 0:
            res = r[0].replace('61','')
        else:
            res = ''
    w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

k.close()
w.close()