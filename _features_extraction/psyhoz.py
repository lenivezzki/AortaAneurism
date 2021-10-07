r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('соматогенный_психоз.txt', 'w')

import re


docs = ['ПОСЛЕОПЕРАЦИОННЫЙ_ПЕРИОД',
        'ПОСЛЕОПЕРАЦИОННЫЕ_ОСЛОЖНЕНИЯ',
        'ПРОТОКОЛ_ОПЕРАЦИИ_ЗАМЕСТИТЕЛЬНОЙ_ПОЧЕЧНОЙ_ТЕРАПИИ',
        'ПОСЛЕОПЕРАЦИОННЫЙ_ДНЕВНИК',
        'ПРОТОКОЛ_ОПЕРАЦИИ_ЗАМЕСТИТЕЛЬНОЙ_ПОЧЕЧНОЙ_ТЕРАПИИ_(MPS+PE)',
        'ПРОТОКОЛ_ИНТРАОПЕРАЦИОННОГО_НЕЙРОФИЗИОЛОГИЧЕСКОГО_МОНИТОРИНГА',
        'ДНЕВНИК_НАБЛЮДЕНИЙ_В_РЕАНИМАЦИОННОМ_ОТДЕЛЕНИИ',
        'ОСМОТР_ХИРУРГА',
        'ДНЕВНИК_Хирургия_№1',
        'ЗАПИСЬ_ПРИ_ПЕРЕВЯЗКЕ',
        'ДНЕВНИК_НАБЛЮДЕНИЙ_В_РЕАНИМАЦИОННОМ_ОТДЕЛЕНИИ_ПИТ№7',
        'ОСМОТР_РЕАНИМАТОЛОГА.',
        'ПОСЛЕОПЕРАЦИОННЫЕ_ОСЛОЖНЕНИЯ',
        'ВЫПИСНОЙ_ЭПИКРИЗ',
        'ПОЯСНЕНИЯ_К_НАЗНАЧЕНИЮ',
        'ДНЕВНИК_ССХ3']

for line in r.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = text.replace('ё', 'е')
    text = text.replace('депрессии st', '')
    text = text.replace('депрессия st', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('постнаркозной депрессии', '')
    text = text.replace('постнаркозная депрессия', '')
    text = text.replace('депрессивного', 'депрессия')
    text = text.replace('депрессивна', 'депрессия')
    text = text.replace('депрессивен', 'депрессия')
    text = text.replace('депрессии сегмента', '')
    text = re.sub(r' +', ' ', text)
    text = re.sub(r'неврологическ...? дефицит[а-я]?[а-я]?','невролгический дефицит', text)
    res = '0'

    if a[10] not in docs:
        continue

    if (text.find(' психоз') != -1):
        res = '1'
    if (text.find(' депрессия') != -1):
        res = '1'
    if (text.find('невролгический дефицит') != -1):
        res = '1'
    if res == '1':
        w.write(a[1] + '\t' + a[3] + '\t' + a[10] + '\t' + res + '\n')

r.close()
w.close()