f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('мочевина.txt', 'w')

import re

def var1(text):
    return re.findall(r'мочевина ?\d+[.,]?\d+? ?м?м?о?л?ь?', text) #мочевина 0,131 ммоль



def check(res):
    if res != '':
        try:
            if (float(res) > 70.0):
                return 0
        except ValueError:
            print('ferror')
    return 1

for line in f.readlines():
    a = line.split('\t')
    if a[10].find('РЕКОМЕНДАЦИ') != -1:
        continue
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = text.replace('до', '')

    text = text.replace('дата', '')
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('мочевины', 'мочевина')

    res=''


    #мочевина 13,1 ммоль/г
    res1 = var1(text)
    if len(res1) > 0:
        res = re.sub(r'[^0-9.,]+', '', res1[len(res1) - 1])
        res = res.replace(',', '.')


    if check(res) == 0:
        if res[:2] == '61':
            res = res[2:]
        else:
            res=''

    w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()