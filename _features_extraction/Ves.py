r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('вес.txt', 'w')

#r = open('data.txt', 'r')
#w = open('rost_beta.txt', 'w')

import re


def var1(text):
    res = re.findall(r' вес \d\d\d?', text)
    return res

def var2(text):
    res = re.findall(r' вес кг \d\d\d?', text)
    return res

def var3(text):
    res = re.findall(r' вес\d\d\d?', text)
    return res

def isRestrict(res):
    if res != '':
        if int(res) > 290:
            return 1000
        else:
            if int(res) < 32:
                return -1000
            else:
                return 0
    else:
        return 10


for line in r.readlines():
    a = line.split('\t')
    text = a[11].lower()
    text = text.replace('293msl', ' ')
    text = text.replace('ves', 'вес')
    text = text.replace('rost', 'рост')
    text = re.sub(r'id[a-z0-9]+ ', ' ', text)
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
        if (len(res1) > 0 & len(res2) > 0) | (len(res1) > 0 & len(res3) > 0) | (len(res2) > 0 & len(res3) > 0):
            res = ''
        if (isRestrict(res) == 1000) | (isRestrict(res) == -1000):
            res = ''
    w.write(a[1] + '\t'+a[3]+'\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()