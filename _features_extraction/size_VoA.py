f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('размер_восход_аорты.txt', 'w')

import re

def var1(text):
    return re.findall(r'восходящий_отдел_аорты \d+ мм', text)

def var2(text):
    return re.findall(r'восходящий_отдел_аорты \d+ \d мм', text)

def var3(text):
    return re.findall(r'восходящий_отдел_аорты \d[.,]?\d? ?с?м?', text)

def var4(text):
    return re.findall(r'\d[.,]?\d? восх\. отд\. см ла', text)

def var5(text):
    return re.findall(r'восходящий_отдел_аорты \d+ х\d мм', text)

def var6(text):
    return re.findall(r'восходящий_отдел_аорты \d[.,]?\d? х\d[.,]?\d? cм', text)

def var6(text):
    return re.findall(r'восходящий_отдел_аорты \d[.,]?\d? х\d[.,]?\d? мм', text)


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
    try:
        num1 = float(nums[0])
        num2 = float(nums[1])
    except ValueError:
        print(res)
        return res
    return str((num1+num2)/2.0)

def check(res):
    if res != '':
        try:
            if (float(res) > 106.0) | (float(res) < 20.0):
                return 0
        except ValueError:
            print('ferror')
    return 1

for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    if (a[2] == 'GACAd[АAAAAAENADxcA!AP'):
        print()
    text = text.lower()
    text = text.replace('x', 'х') #англ -> рус
    text = text.replace('294m', '') #maorta_sm
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = text.replace(' тдела', ' отдела')
    text = text.replace('аневризма восходящей аорты до', 'восходящий_отдел_аорты')
    text = text.replace('аневризме восходящего отдела аорты размер аорты до', 'восходящий_отдел_аорты')
    text = text.replace(' до ', ' ')
    text = re.sub(r' +', ' ', text)
    text = text.replace('диаметром', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('восходящей части грудного отдела аорты', 'восходящий_отдел_аорты')
    text = text.replace('восходящая часть аорты', 'восходящий_отдел_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('aвосх.', 'восходящий_отдел_аорты')
    text = text.replace('на уровне фиброзного кольца', 'восходящий_отдел_аорты')
    text = text.replace('расширение воа', 'восходящий_отдел_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('расширение восходящего отдела грудной аорты максимальным','восходящий_отдел_аорты')
    text = text.replace('расширение её в восх отделе', 'восходящий_отдел_аорты')
    text = text.replace('восх ао', 'восходящий_отдел_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('восх отдел','восходящий_отдел_аорты')
    text = text.replace('восх. отдела аорты', 'восходящий_отдел_аорты')
    text = text.replace('аорта расширена максимально в восходящем отделе', 'восходящий_отдел_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('аорта расширена в восходящем отделе', 'восходящий_отдел_аорты')
    text = text.replace('на уровне бифуркации легочного ствола', 'восходящий_отдел_аорты')
    text = text.replace('с расширением на уровне бифуркации ла', 'восходящий_отдел_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('перед отхождением бцс', 'восходящий_отдел_аорты')
    text = text.replace('перед отхождением лпка', 'восходящий_отдел_аорты')
    text = text.replace('после отхождения лпка', 'восходящий_отдел_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('восходящая аорта на уровне синусов вальсальвы', 'восходящий_отдел_аорты')
    text = text.replace('восходящая аорта на уровне синотубулярного соединения', 'восходящий_отдел_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('восходящий отдел аорты перед отхождением плечеголовного ствола', 'восходящий_отдел_аорты')
    text = text.replace('восходящая аорта расширена', 'восходящий_отдел_аорты')
    text = re.sub(r' +', ' ', text)
    text = text.replace('аорты составляет восходящей', 'восходящий_отдел_аорты')
    text = text.replace('на уровне бифуркации легочной артерии', '')
    text = text.replace('на уровне устья левой подключичной артерии', '')
    text = text.replace('на уровне устья левой подключичной артерии', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('синотубулярное соединение', 'восходящий_отдел_аорты')
    text = text.replace('синотубулярное соединение', 'восходящий_отдел_аорты')
    text = re.sub(r'брахиоцефальн...? ствол.?', 'восходящий_отдел_аорты', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('cинотубулярная зона', 'восходящий_отдел_аорты')
    text = text.replace('на уровне легочного ствола', 'восходящий_отдел_аорты')
    text = text.replace('восходящей части дуги', 'восходящий_отдел_аорты')
    text = re.sub(r' +', ' ', text)

    text = text.replace('восходящего отдела аорты', 'восходящий_отдел_аорты')
    text = text.replace('восходящем отделе аорты', 'восходящий_отдел_аорты')
    text = text.replace('восходящий отдел аорты', 'восходящий_отдел_аорты')
    text = text.replace('восходящая аорта', 'восходящий_отдел_аорты')

    #6,6 восх. отд. см

    res = ''

    res4 = var4(text)
    if len(res4) > 0:
        res = re.sub(r'[^0-9,]+', '', res4[len(res4)-1])
        res = cm_to_mm(res)

    res3 = var3(text)
    if len(res3) > 0:
        res = re.sub(r'[^0-9.,]+', '', res3[len(res3) - 1])
        res = cm_to_mm(res)

    res2 = var2(text)
    if len(res2) > 0:
        res = re.sub(r'[^0-9 ]+', '', res2[len(res2) - 1])
        res = res.strip()
        r = res.split(' ')
        try:
            if float(r[0]) > float(r[1]):
                res = r[0]
            else:
                res = r[1]
        except ValueError:
            print('ferror')

    #40 мм в цикле
    res1 = var1(text)
    if len(res1) > 0:
        max = 0.0
        for r in res1:
            r = re.sub(r'[^0-9.,]+', '', r)
            if max < float(r):
                max = float(r)
        if max != 0.0:
            res = str(max)

    #несколько 6,5 х6,6 см балждалдв
    res6 = var6(text)
    if len(res6) > 0:
        max = 0.0
        for r in res6:
            r = re.sub(r'[^0-9 .,х]+', '', r)
            r = re.sub(r' +', '', r)
            r = r[1:]
            r = count_aver_out_of_two(r)
            if max < float(r):
                max = float(r)
        if max != 0.0:
            res = str(max)
            res = cm_to_mm(res)

    # 34 x24 мм
    res5 = var5(text)
    if len(res5) > 0:
        res = re.sub(r'[^0-9.,х ]+', '', res5[len(res5) - 1])
        res = res[1:]
        res = count_aver_out_of_two(res)




    if check(res) == 0:
        if check(res[:2]) == 1:
            res = res[:2]
        else:
            res=''
    if res !='':
        w.write(a[1] + '\t' +a[3]+'\t'+ a[10] + '\t' + res + '\n')

f.close()
w.close()