k = open('patients_with operations_dataset_clean.txt', 'r')
w = open('синус_вальсальвы.txt', 'w')

import re

def var1(text):
    return re.findall(r'вальсальвы \d+[.,]?\d? х\d+[.,]?\d? ?м?м?', text)

def var2(text):
    return re.findall(r'вальсальвы \d[,.]?\d+? х\d[.,]?\d+? см', text)

def var3(text):
    return re.findall(r'вальсальвы ?\d+ мм', text)

def var4(text):
    return re.findall(r'вальсальвы \d+[.,]?\d? \d+[.,]?\d? ?м?м?', text)

def var5(text):
    return re.findall(r'вальсальвы \d+[,.]\d+[.,]\d см', text)

def var6(text):
    return re.findall(r'вальсальвы \d+[.,]\d+ см', text)

def var7(text):
    return re.findall(r'аорт. до \d\d мм. на уровне синус..? вальсальвы', text)

def var8(text):
    return re.findall(r'аорт. до \d\d мм. на уровне синус..? вальсальвы', text)

def var9(text):
    return re.findall(r'вальсальвы \d+[,.]\d+ \d+[.,]\d см', text)



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
        if float(res) > 80.0:
            return 0
    return 1


for line in k.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    if a[2] == 'GACAd9тAABAAA21:24A-AJ':
        print()
    text = text.replace('x', 'х') #англ -> рус
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('на уровне синусов', 'синусов вальсальвы')
    #text = text.raplace('синусов вальсальвы')
    text = text.replace('на уровне коронарных синусов', 'синусов вальсальвы')
    text = text.replace('вальсалвы', 'вальсальвы')
    text = re.sub(r' +', ' ', text)
    text = text.replace('вальсальвы до', 'вальсальвы')
    text = re.sub(r' +', ' ', text)
    text = text.replace('вальсальвы аневризматически расширен до', 'вальсальвы')
    text = text.replace('вальсальвы диаметром', 'вальсальвы')
    text = re.sub(r' +', ' ', text)
    text = text.replace('синусоваорты', 'синусов вальсальвы')
    text = re.sub(r' +', ' ', text)
    text = text.replace('ритм синусовый аорта', 'синусов вальсальвы')
    text = re.sub(r' +', ' ', text)

    res = ''

    res7 = var7(text)
    if len(res7) > 0:
        res = re.sub(r'[^0-9]+', '', res7[len(res7)-1])
#        if len(res7) > 1:
#            print('')

    res6 = var6(text)
    if len(res6) > 0:
        res = re.sub(r'[^0-9.,]+', '', res6[len(res6)-1])
        res = cm_to_mm(res)
#        if len(res6) > 1:
#            print('')

    res9 = var9(text)
    if len(res9) > 0:
        res = re.sub(r'[^0-9.,]+', '', res9 [len(res9) - 1])
        res = cm_to_mm(res[3:6])

    res5 = var5(text)
    if len(res5) > 0:
        res = re.sub(r'[^0-9.,]+', '', res5[len(res5)-1])            #задать вопрос, пока беру типа 4,44,5 см это 44,45 мм
        res = cm_to_mm(res[:-2])
#        if len(res5) > 1:
#            print('')

    res4 = var4(text)
    if len(res4) > 0:
        res = re.sub(r'[^0-9 ]+', '', res4[len(res4)-1])
        res = res.strip()
        r = res.split(' ')
        try:
            if float(r[0]) > float(r[1]):
                res = r[0]
            else:
                res = r[1]
        except ValueError:
            print('ferror')
#        if len(res4) > 1:
#            print('')

    res3 = var3(text)
    if len(res3) > 0:
        res = re.sub(r'[^0-9]+', '', res3[len(res3)-1])
#        if len(res3) > 1:
#            print('')

    res1 = var1(text)
    if len(res1) > 0:
        res = re.sub(r'[^0-9х,. ]+', '', res1 [len(res1) - 1])
        res = count_aver_out_of_two(res)

    res2 = var2(text)
    if len(res2) > 0:
        res = re.sub(r'[^0-9х .,]+', '', res2[len(res2)-1])
        res = count_aver_out_of_two(res)
        res = cm_to_mm(res)

#        if len(res2) > 1:
#            print('')


#        if len(res1) > 1:
#            print('')
    if check(res) == 0:
        res=''
    if res != '':
        w.write(a[1] + '\t' +a[3]+'\t' + a[10] + '\t' + res + '\n')

k.close()
w.close()