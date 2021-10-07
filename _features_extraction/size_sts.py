f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('размер_стс_аорты.txt', 'w')

import re

def var1(text):
    return re.findall(r' стс \d+ мм', text)

def var2(text):
    return re.findall(r' стс \d+ х \d+ мм', text)




def count_aver_out_of_two(res):
    res = res.replace(' ', '')
    res = res.replace(',', '.')
    nums = res.split('х')
    num1 = float(nums[0])
    num2 = float(nums[1])
    return str((num1+num2)/2.0)

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

def check(res):
    if res != '':
        try:
            if float(res) > 55.0:
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
    text = text.replace('диаметр', '')
    text = text.replace('диаметром', '')
    text = re.sub(r' +', ' ', text)

    text = text.replace('', '')


    res = ''

    #33 мм
    res1 = var1(text)
    if len(res1) > 0:
        res = re.sub(r'[^0-9,.]+', '', res1[len(res1) - 1])
        res = res.replace(',', '.')
        try:
            if float(res) > 999.0:  # 3533 мм
                if float(res[:2]) > float(res[2:]):
                    res = res[:2]
                else:
                    res = res[2:]
        except ValueError:
            print('ferror')

    #33 x 37 мм
    res2 = var2(text)
    if len(res2) > 0:
        res = re.sub(r'[^0-9,.х ]+', '', res2[len(res2) - 1])
        res = re.sub(r' +', ' ', res)
        res = count_aver_out_of_two(res)








    w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()