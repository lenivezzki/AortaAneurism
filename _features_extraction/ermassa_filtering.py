f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('эрмасса_фильтр.txt', 'w')

import re

docs = ['ПРОТОКОЛ_ПЕРЕЛИВАНИЯ_КРОВИ_И_КОМПОНЕНТОВ_КРОВИ',
        'ТРЕБОВАНИЕ_на_выдачу_ГТС']

for line in f.readlines():
    a = line.split('\t')
    if a[10] not in docs:
        continue
    text = ' '+a[11]+' '
    text = text.lower()
    text = re.sub(r'293pan\d+', '', text)
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('требуемая гемотрансфузионная среда наименование среды','')
    text = re.sub(r'компоненты номер компонента штрих код \d+ сегмент ...? ','',text)
    text = re.sub(r' +', ' ', text)
    if text.find(' эр') != -1:
        w.write(a[0]+'\t'+a[3]+'\t'+a[4]+'\t'+a[10]+'\t'+text+'\n')
w.close()
f.close()
