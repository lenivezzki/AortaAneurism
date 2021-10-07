f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('умеренная_гипотермия.txt', 'w')    #Глубокая гипотермия 14.1-20 ℃

import re

def var1(text):
    return re.findall(r' гипотерми. \d+[.,]?\d+?', text) #гипотермии(я) 27

def var2(text):
    return re.findall(r' умеренн.. гипотерм..', text) #умеренная гипотермии


def check(res):
    if res != '0':
        try:
            if float(res) > 40.0:
                return 0
        except ValueError:
            print('ferror')
    return 1

docs = ['ПРОТОКОЛ_ОПЕРАЦИИ.',
        'ПРЕДОПЕРАЦИОННЫЙ_ЭПИКРИЗ',
        'ПРОТОКОЛ_ОПЕРАЦИИ',
        'ПОСЛЕОПЕРАЦИОННЫЙ_ПЕРИОД',
        'ПРОТОКОЛ_ОПЕРАЦИИ_НА_СЕРДЦЕ',
        'ПРОТОКОЛ_ОПЕРАЦИИ_(ИМПЛАНТАЦИЯ_ИКД) первичная без смены ИКД',
        'ПРОТОКОЛ_ОПЕРАЦИИ_(ИМПЛАНТАЦИЯ_ЭКС) первичная без смены ЭКС',
        'ОСМОТР_КАРДИОЛОГА_ССХ_ПЕРЕД_ОПЕРАЦИЕЙ',
        'ПРОТОКОЛ_ОПЕРАЦИИ_(НА_СРЕДОСТЕНИИ)',
        'ОПЕРАЦИЯ_НА_СОСУДАХ_ШЕИ._КАРОТИДНАЯ_ЭНДАТЕРЭКТОМИЯ',
        'ОПЕРАЦИЯ_АРИТМОЛОГИЧЕСКАЯ_(ИМПЛАНТАЦИЯ_УСТРОЙСТВ)',
        'ОПЕРАЦИЯ_АРИТМОЛОГИЧЕСКАЯ_(РЧ/РЧА)',
        'ПОСЛЕОПЕРАЦИОННЫЕ_ОСЛОЖНЕНИЯ',
        'ПРОТОКОЛ_ОПЕРАЦИИ_ЗАМЕСТИТЕЛЬНОЙ_ПОЧЕЧНОЙ_ТЕРАПИИ',
        'ПРОТОКОЛ_ОПЕРАЦИИ_(РЧА)',
        'ПОСЛЕОПЕРАЦИОННЫЙ_ДНЕВНИК',
        'ПРОТОКОЛ_ОПЕРАЦИИ_(РЕВИЗИЯ)',
        'ПРОТОКОЛ_ОПЕРАЦИИ_ЗАМЕСТИТЕЛЬНОЙ_ПОЧЕЧНОЙ_ТЕРАПИИ_(MPS+PE)',
        'ПРОТОКОЛ_ИНТРАОПЕРАЦИОННОГО_НЕЙРОФИЗИОЛОГИЧЕСКОГО_МОНИТОРИНГА']

for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    #if text.find('Гипотермия 18') != -1:
    #    print('warr')
    text = text.lower()
    text = text.replace('c','с') #англ -> рус
    text = re.sub(r'[^а-я0-9 ё.,]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = text.replace(' до ', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('гипотермия.', 'гипотермия')
    res = '0'

    if a[10] not in docs:
        continue
    c = '0'
    res1 = var1(text)
    if len(res1) > 0:
        res = re.sub(r'[^0-9.,]+', '', res1[len(res1) - 1])
        res = res.replace(',','.')
        try:
            if (float(res) > 20.0) & (float(res) <= 28.0):
                c = '1'
            else:
                c = '0'
        except ValueError:
            print('ferror')

    res2 = var2(text)
    if len(res2) > 0:
        c = '1'


    if check(res) == 0:
        if (res == '200') | (res == '180'):
            res = res[:2]
            try:
                if (float(res) > 20.0) & (float(res) <= 28.0):
                    c = '1'
                else:
                    c = '0'
            except ValueError:
                print('ferror')
        else:
            c = '0'
    res = c
    w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()