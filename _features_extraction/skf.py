f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('СКФ.txt', 'w')

import re

def var1(text):
    return re.findall(r'скф ?\d+[.,]?\d+? ?м?л?', text) #скф 0,131 мл/мин

def var2(text):
    return re.findall(r'скф ?\d+[.,]?\d+? л', text) #скф 0,131 л/мин



def l_to_ml(res):
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
            if (float(res) > 100.0):
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
    text = text.replace('составляет ', '')
    text = text.replace('60 62 ', '')
    text = text.replace('до', '')
    text = text.replace('дата', '')
    text = text.replace('скф по mdrd', 'скф')
    text = text.replace('скф по формуле mdrd', 'скф')
    text = text.replace('скф по ckd-epi', 'скф')
    text = text.replace('по cockroft=gault', '')
    text = text.replace('ckd-epi', 'скф')
    text = text.replace('ckd-epf', 'скф')
    text = text.replace('ml', 'мл')
    text = text.replace('скф 1 раз в 6 месяцев', '')
    text = re.sub(r'[^а-я0-9 ё,.]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('клиренс креатинина', 'скф')
    text = text.replace('клиренса', 'скф')
    text = text.replace('скоростьклубочковойфильтрации', 'скф')
    text = text.replace('скорость клубочковой фильтрации', 'скф')
    text = text.replace('скф снижена', 'скф')
    text = text.replace('скф менее', 'скф')
    text = text.replace('скф на сегодня', 'скф')
    text = re.sub(r'скф от 20\d\d', 'скф', text)
    text = re.sub(r'скф на \d\d\.\d\d\.\d\d\d?\d? ?г?\.?', 'скф', text)
    text = re.sub(r'скф от \d\d\.\d\d\.\d\d\d?\d? ?г?\.?', 'скф', text)
    text = re.sub(r' +', ' ', text)

    res=''


    # скф 13,1 мл/мин
    res1 = var1(text)
    if len(res1) > 0:
        res = re.sub(r'[^0-9.,]+', '', res1[len(res1) - 1])
        res = res.replace(',', '.')


    #скф 1,31 л/мин
    res2 = var2(text)
    if len(res2) > 0:
        res = re.sub(r'[^0-9.,]+', '', res2[len(res2) - 1])
        res = l_to_ml(res)



    if check(res) == 0:
        if res[:2] == '61':
            res = res[2:]
        else:
            res = ''

    if (text.find('скф') != -1) & (res==''):
        print(a[1])

    w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()