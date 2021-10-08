f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('креатинин.txt', 'w')

import re

def var1(text):
    return re.findall(r'креатинин ?\d+[.,]?\d+? ?м?к?м?о?л?ь?', text) #креатинин 48.0 мкмоль



def check(res):
    if res != '':
        try:
            if (float(res) > 3000.0) | (float(res) < 1):
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
    text = text.replace('60 62 ', '')
    text = text.replace('до', '')
    text = text.replace('дата', '')
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('креатинина сыворотки', 'креатинин')
    text = text.replace('клиренс креатинина', '')
    text = text.replace('креатинина крови', 'креатинин')
    text = text.replace('креатинина', 'креатинин')
    text = re.sub(r' +', ' ', text)

    res=''


    #креатинин 13,1 мкмоль/г
    res1 = var1(text)
    if len(res1) > 0:
        res = re.sub(r'[^0-9.,]+', '', res1[len(res1) - 1])
        res = res.replace(',', '.')


    if check(res) == 0:
        if res[:2] == '61':
            res = res[2:]
        else:
            res=''

    if res != '':
        w.write(a [1] + '\t' + a [3] + '\t' + a [10] + '\t' + res + '\n')

f.close()
w.close()