f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('размер_дуги_аорты.txt', 'w')

import re

def var1(text):
    return re.findall(r'дуга_аорты \d+ ?м?м?', text)

def var2(text):
    return re.findall(r'дуга_аорты \d+[.,]\d+ с?м', text)

def var3(text):
    return re.findall(r'дуга_аорты \d+ \d+ мм', text)

def var4(text):
    return re.findall(r'дуга_аорты \d+[.,]\d+ см \d+[.,]\d+ см', text)

def var5(text):
    return re.findall(r'дуга_аорты \d+[.,]\d+ х\d+[.,]\d+ см \d+[.,]\d+ х\d+[.,]\d+ см', text)

def var6(text):
    return re.findall(r'дуга_аорты \d+ х\d+ мм', text)

def var7(text):
    return re.findall(r'дуга_аорты \d+[.,]\d+ см дуга_аорты \d+[.,]\d+ см', text)

def var8(text):
    return re.findall(r'дуга_аорты \d+[.,]\d+ х\d+ мм \d+[.,]\d+ х\d+ мм', text)

def var11(text):
    return re.findall(r'дуга_аорты \d+[.,]\d+[.,]\d+ с?м', text)

def var10(text):
    return re.findall(r'дуга_аорты \d+[.,]\d+ х\d+[.,]\d+', text)


def cm_to_mm(res):
    res = res.replace(',', '.')
    if res.find('х') == -1:
        try:
            res = str(float(res) * 10.0)
        except ValueError:
            print(res)
    else:
        res = res.replace('.', '')
    return res

def count_aver_out_of_two(res):
    res = res.replace(' ', '')
    res = res.replace(',', '.')
    nums = res.split('х')
    num1 = float(nums[0])
    num2 = float(nums[1])
    return str((num1+num2)/2.0)

def check(res):
    if res != '':
        try:
            if (float(res) > 80.0) | (float(res) < 20.0):
                return 0
        except ValueError:
            print('ferror')
    return 1



for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = text.replace('x', 'х') #англ -> рус
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    if a[2] == 'GACAIм\AAEAAcNABbQAaAP':
        print()
    text = text.replace('диаметр дуги аорты около', 'дуга_аорты')
    text = text.replace('диаметр', '')
    text = text.replace('диаметром', '')
    text = text.replace('на уровне дуги и нисходящего отдела аорты на протяжении 14,5 см аорта расширена','дуга_аорты')
    text = text.replace('дистальнее устья левой подключичной артерии аорта несколько расширена максимально',
                        'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('дуга аорты до бцс', 'дуга_аорты')
    text = text.replace('аорта расширена в восходящем отделе, в области дуги', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('дуга аорты после отхождения плечеголовного ствола с лоса', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('дуга аорты после отхождения плечеголовного ствола', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('после отхождения плечеголовного ствола','дуга_аорты')
    text = text.replace('левой общей сонной артерии', 'лоса')
    text = text.replace('л оса ', 'лоса ')
    text = text.replace('дуга аорты перед отхождением лоса','дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('дуга аорты после отхождением лоса', 'дуга_аорты')
    text = text.replace('дуга аорты перед отхождением бцс', 'дуга_аорты')
    text = text.replace('дуга аорты расширена до', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('дуга аорты после отхождения левой оса', 'дуга_аорты')
    text = text.replace(' дуга до', ' дуга_аорты ')
    text = text.replace(' до ', ' ')
    text = re.sub(r' +', ' ', text)
    text = text.replace('проксимальнее устья левой подключичной артерии', 'дуга_аорты')
    text = text.replace('дистальнее устья левой подключичной артерии', 'дуга_аорты')
    text = text.replace('дистальнее устья плечеголовного ствола', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('дистальнее устья лоса', 'дуга_аорты')
    text = text.replace('дистальнее устья бцс', 'дуга_аорты')
    text = text.replace('проксимальнее устья лоса', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('проксимальнее устья лпка', 'дуга_аорты')
    text = text.replace('дуга аорты после отхождения п оса', 'дуга_аорты')
    text = text.replace('дуга аорты перед отхождением л пка', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('дуга аорты дистальнее левой подключичной артерии', 'дуга_аорты')
    text = text.replace('после отхождения плечеголовного ствол', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)

    text = text.replace('на уровне дуги', 'дуга_аорты')
    text = text.replace('дуга аорты после отхождения плечеголовного ствола и лоса', 'дуга_аорты')
    text = text.replace('после отхождения плечеголовного ствола', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('после отхождения брахиоцефального ствола', 'дуга_аорты')
    text = text.replace('после отхождения левой подключичиной артерии', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('проксимальнее устья левой пка', 'дуга_аорты')
    text = text.replace('дуга не расширена','дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('в области дуги', 'дуга_аорты')
    text = text.replace('восходящей части дуги', '')
    text = text.replace('дуги и нисх. аорты', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('дуга аорты между левой оса и левой пка', 'дуга_аорты')
    text = text.replace('дуги аорты на уровне левой пка', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('аневризма дуги аорты с максимальным', 'дуга_аорты')
    text = text.replace('дуга аорты проксимальнее лпка', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('перед отхождением бцс','дуга_аорты')
    text = text.replace('после отхождения бцс', 'дуга_аорты')
    text = text.replace('проксимальнее устья бцс','дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('аорты на уровне плечеголовного ствола', 'дуга_аорты')
    text = text.replace('аорты на уровне отхождения левой подключичной артерии', 'дуга_аорты')
    text = text.replace('аорты на уровне перешейка', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('перед устьем брахиоцефального ствола с лоса', 'дуга_аорты')
    text = text.replace('после общего вестибюля бцс с лоса', 'дуга_аорты')
    text = text.replace('перед лпка', 'дуга_аорты')
    text = text.replace('после лпка', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('проксимальнее бцс','дуга_аорты')
    text = text.replace('дистальнее левой пка', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('на уровне устья бцс', 'дуга_аорты')
    text = text.replace('на уровне устья лпка', 'дуга_аорты')
    text = text.replace('на уровне устья брахиоцефального ствола', 'дуга_аорты')
    text = text.replace('на уровне устья левой подключичной артерии', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('дистальнее устья лпка', 'дуга_аорты')
    text = text.replace('перед бцс', 'дуга_аорты')
    text = text.replace('кпереди от устья бцс','дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('кзади от устья левой подключичной артерии', 'дуга_аорты')
    text = text.replace('на дугу аорты максимальное расширение', 'дуга_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('проксимальнее отхождения левой подключичной артерии','дуга_аорты')
    text = text.replace('на дугу аорты максимальное расширение', 'дуга_аорты')
    text = text.replace('после отхождения лоса','дуга_аорты')


    text = re.sub(r' +', ' ', text)

    text = text.replace('дуга ао ', 'дуга_аорты')
    text = text.replace('дуга аорты', 'дуга_аорты')
    text = text.replace(' дуга ', ' дуга_аорты ')
    text = re.sub(r' +', ' ', text)

    fin = '-1.0'
    res = ''

    #if (text.find('дуга') != -1) & (a[1] == 'GACAL({'):
    #    print(a[1])

    res5 = var5(text)
    if len(res5) > 0:
        res = re.sub(r'[^0-9х .,]+', '', res5[len(res5)-1])
        res = re.sub(r' +', ' ', res)
        res = res.strip()
        r = res.split(' ')
        r[0] = count_aver_out_of_two(' '.join(r[:2]))
        r[1] = count_aver_out_of_two(' '.join(r[2:]))
        if r[0] > r[1]:
            res = r[0]
        else:
            res = r[1]
        res = cm_to_mm(res)
        if float(res) > float(fin):
            fin = res

    res4 = var4(text)
    if len(res4) > 0:
        res = re.sub(r'[^0-9 .,]+', '', res4[len(res4)-1])
        res = re.sub(r' +', ' ', res)
        res = res.strip()
        r = res.split(' ')
        if r[0] > r[1]:
            res = r[0]
        else:
            res = r[1]
        res = cm_to_mm(res)
        if float(res) > float(fin):
            fin = res

    res3 = var3(text)
    if len(res3) > 0:
        res = re.sub(r'[^0-9 ]+', '', res3[len(res3) - 1])
        res = res.strip()
        r = res.split(' ')
        try:
            if float(r[0]) > float(r[1]):
                res = r[0]
            else:
                res = r[1]
        except ValueError:
            print('ferror')
        if float(res) > float(fin):
            fin = res

    res2 = var2(text)
    if len(res2) > 0:
        max = 0.0
        for r in res2:
            r = re.sub(r'[^0-9 .,]+', '', r)
            r = re.sub(r' +', ' ', r)
            r = r.replace(',', '.')
            if max < float(r):
                max = float(r)
        if max != 0.0:
            res = str(max)
            res = cm_to_mm(res)
        if float(res) > float(fin):
            fin = res

    res1 = var1(text)
    if len(res1) > 0:
        max = 0.0
        for r in res1:
            r = re.sub(r'[^0-9.,]+', '', r)
            r = re.sub(r' +', ' ', r)
            if max < float(r):
                max = float(r)
        if max != 0.0:
            res = str(max)
        if float(res) > float(fin):
            fin = res

    res6 = var6(text)
    if len(res6) > 0:
        max = 0.0
        for r in res6:
            r = re.sub(r'[^0-9х .,]+', '', r)
            r = re.sub(r' +', ' ', r)
            r = count_aver_out_of_two(r)
            if max < float(r):
                max = float(r)
        if max != 0.0:
            res = str(max)
        if float(res) > float(fin):
            fin = res

    res8 = var8(text)
    if len(res8) > 0:
        res = re.sub(r'[^0-9х .,]+', '', res8[len(res8)-1])
        res = re.sub(r' +', ' ', res)
        res = res.strip()
        res = res.replace(',', '.')
        r = res.split(' ')
        r[0] = count_aver_out_of_two(' '.join(r[:2]))
        r[1] = count_aver_out_of_two(' '.join(r[2:]))
        if r[0] > r[1]:
            res = r[0]
        else:
            res = r[1]
        if float(res) > float(fin):
            fin = res

    res7 = var7(text)
    if len(res7) > 0:
        res = re.sub(r'[^0-9 .,]+', '', res7[len(res7)-1])
        res = re.sub(r' +', ' ', res)
        res = res.strip()
        res = res.replace(',', '.')
        r = res.split(' ')
        if r[0] > r[1]:
            res = r[0]
        else:
            res = r[1]
        res = cm_to_mm(res)
        if float(res) > float(fin):
            fin = res

    res9 = var2(text)
    if len(res9) > 0:
        max = 0.0
        for r in res9:
            r = re.sub(r'[^0-9 .,]+', '', r)
            r = re.sub(r' +', ' ', r)
            r = r.replace(',', '.')
            if max < float(r):
                max = float(r)
        if max != 0.0:
            res = str(max)
            res = cm_to_mm(res)
        if float(res) > float(fin):
            fin = res

    res10 = var10(text)
    if len(res10) > 0:
        max = 0.0
        for r in res10:
            r = re.sub(r'[^0-9х .,]+', '', r)
            r = re.sub(r' +', ' ', r)
            r = count_aver_out_of_two(r)
            if max < float(r):
                max = float(r)
        if max != 0.0:
            res = str(max)
            res = cm_to_mm(res)
        if float(res) > float(fin):
            fin = res

    res11 = var11(text)
    if len(res11) > 0:
        max = 0.0
        for r in res11:
            r = re.sub(r'[^0-9 .,]+', '', r)
            r = re.sub(r' +', '', r)
            r = r.replace(',', '.')
            r = r.split('.')
            r = '.'.join(r[:-1])
            if max < float(r):
                max = float(r)
        if max != 0.0:
            res = str(max)
            res = cm_to_mm(res)
        if float(res) > float(fin):
            fin = res

    if check(fin) == 0:
        if check(fin[:2]) == 1:
            fin = fin[:2]
        else:
            fin=''

    if (fin != '-1.0') & (fin != ''):
        w.write(a [1] + '\t' + a [3] + '\t' + a [10] + '\t' + fin + '\n')

f.close()
w.close()
