f = open('patients_only operation.txt', 'r')
w = open('окклюзия_аорты.txt', 'w')

import re

def var1(text):
    return re.findall(r'время пережатия аорты ?\d+ ?м?и?н?', text)
def var2(text):
    return re.findall(r'аноксия ?\d+', text)
def var3(text):
    return re.findall(r'время [а-я]+ аорт ?\d+', text)
def var4(text):
    return re.findall(r'пережатие аорты ?\d+', text)
def var5(text):
    return re.findall(r'время ишемии ?\d+ ?м?и?н?', text)
def var6(text):
    return re.findall(r'ишемия ?\d+ ?мин', text)


for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = re.sub(r' +', ' ', text)
    res = '0'

    res6 = var6(text)
    if len(res6) > 0:
        res = re.sub(r'[^0-9]+', '', res6 [0])

    res5 = var5(text)
    if len(res5) > 0:
        res = re.sub(r'[^0-9]+', '', res5 [0])

    res4 = var4(text)
    if len(res4) > 0:
        res = re.sub(r'[^0-9]+', '', res4 [0])

    res3 = var3(text)
    if len(res3) > 0:
        res = re.sub(r'[^0-9]+', '', res3[0])
    res2 = var2(text)
    if len(res2) > 0:
        res = re.sub(r'[^0-9]+', '', res2[0])
    res1=var1(text)
    if len(res1) > 0:
        res=re.sub(r'[^0-9]+','',res1[0])

    if res != '0':
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()