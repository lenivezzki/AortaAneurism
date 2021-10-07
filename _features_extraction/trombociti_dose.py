f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('тромбоциты_дозы.txt', 'w')

import re

def var1(text):
    return re.findall(r'тромбоцитный концентрат полученный автоматическим аферезом фильтрованный ед изм мл объем мл кол во ед кол во доз \d+', text)
    #Тромбоцитный_концентрат,_полученный_автоматическим_аферезом,_фильтрованный Ед.изм. мл Объём мл Кол-во ед. 1 Кол-во доз 2 Код среды

def var2(text):
    return re.findall(r'количество перелитой среды л ед \d+ доз', text) #ввл 17 сутки
    #' требуемая гемотрансфузионная среда наименование среды плазма свежезамороженная из дозы крови фильтрованная карантинизованная ед изм мл объем мл кол во ед кол во доз 4'

def var3(text):
    return re.findall(r'тромбоцитный концентрат из дозы крови ед изм мл объем мл кол во ед кол во доз \d+', text)

docs = ['ПРОТОКОЛ_ПЕРЕЛИВАНИЯ_КРОВИ_И_КОМПОНЕНТОВ_КРОВИ',
        'ДНЕВНИК_НАБЛЮДЕНИЙ_В_РЕАНИМАЦИОННОМ_ОТДЕЛЕНИИ',
        'ТРЕБОВАНИЕ_на_выдачу_ГТС']

k = 0
typ = []


for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'293pan\d+', '', text)
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'объем мл \d+', 'объем мл', text)
    text = re.sub(r'кол во ед \d+', 'кол во ед', text)
    text = re.sub(r'\d+ \d+ л \d ед', 'л ед', text)
    text = text.replace('фильтрованный', '')
    text = text.replace('инактивированный аппарат', '')
    text = text.replace('карантинизованная', '')
    text = text.replace('карантинизованная', '')
    text = text.replace('полученная автоматическим аферезом', '')
    text = re.sub(r' +', ' ', text)

    res=''

    if a[10] not in docs:
        continue

    if a[10] == 'ПРОТОКОЛ_ПЕРЕЛИВАНИЯ_КРОВИ_И_КОМПОНЕНТОВ_КРОВИ':
        if k == 0:
            typ = re.findall(r' тк ', text)
            if len(typ) > 0:
                k = 1
        else:
            res2 = var2(text)
            if (len(res2) > 0) & (len(typ) > 0):
                res = re.sub(r'[^0-9]+', '', res2[len(res2) - 1])
                k = 0

    res1 = var1(text)
    if len(res1) > 0:
        res = re.sub(r'[^0-9 ]+', '', res1[len(res1) - 1])
        res = res.strip()
        b = res.split(' ')
        if len(b) > 1:
            res = b[1]
        else:
            res = b[0]

    res3 = var3(text)
    if len(res3) > 0:
        res = re.sub(r'[^0-9 ]+', '', res3[len(res3) - 1])
        res = res.strip()
        b = res.split(' ')
        if len(b) > 1:
            res = b[1]
        else:
            res = b[0]


    w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

f.close()
w.close()