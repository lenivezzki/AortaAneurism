r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('РОСТ_опер.txt', 'w')

#r = open('data.txt', 'r')
#w = open('rost_beta.txt', 'w')

import re

def var1(text):
    res = re.findall(r' рост [12]\d\d', text)
    return res

def var2(text):
    res = re.findall(r' рост см [12]\d\d', text)
    return res

def var3(text):
    res = re.findall(r' рост[12]\d\d', text)
    return res


for line in r.readlines():
    a = line.split('\t')
    text = a[11].lower()
    text = text.replace('rost', 'рост')
    text = re.sub(r'[^а-я0-9 ]', ' ', text)
    text = re.sub(r' +', ' ', text)
    res = ''
    if text.find(' вес') != -1:
        res1 = var1(text)
        res2 = var2(text)
        res3 = var3(text)
        if len(res1) >= 1:
            res = res1[len(res1)-1]
            res = re.sub(r'[^0-9]', '', res)
        else:
            if len(res2) >= 1:
                res = res2[len(res2)-1]
                res = re.sub(r'[^0-9]', '', res)
            else:
                if len(res3) >= 1:
                    res = res3[len(res3) - 1]
                    res = re.sub(r'[^0-9]', '', res)
                else:
                    res = ''
    if res != '':
        w.write(a[1] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()


