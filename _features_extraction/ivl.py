f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('ивл.txt', 'w')

import re

def var1(text):
    return re.findall(r' ивл \d+ сут', text) #ивл 6 суток

def var2(text):
    return re.findall(r' ввл \d+ сут', text) #ввл 17 сутки


for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' .'
    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё.]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('вспомогательная вентиляция легких','ввл')
    text = text.replace('неинвазивная вентиляция легких', 'ввл')
    if (a[10]=='ДНЕВНИК_НАБЛЮДЕНИЙ_В_РЕАНИМАЦИОННОМ_ОТДЕЛЕНИИ') | (a[10]=='ПЕРЕВОДНОЙ_ЭПИКРИЗ_ИЗ_РЕАНИМАЦИОННОГО_ОТДЕЛЕНИЯ'):
        if text.find('дыхание') != -1:
            w.write(a[1] + '\t' + a[3] + '\t' +a[4]+ '\t' + a[10] + '\t' + a[11] + '\n')

    res = ''
    res1 = var1(text)
    if len(res1) > 0:
        res = re.sub(r'[^0-9]+', '', res1[len(res1) - 1])
    res2 = var2(text)
    if len(res2) > 0:
        res = re.sub(r'[^0-9]+', '', res2[len(res2) - 1])
    if res != '':
        w.write(a[1] + '\t' + a[3] + '\t' +a[4]+ '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()