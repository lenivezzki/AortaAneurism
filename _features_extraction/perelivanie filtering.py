f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('переливание_фильтр.txt', 'w')

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
    text = re.sub(r'[^а-я0-9 ё.,]+', ' ', text)
    text = re.sub(r'ё', 'е', text)
    text = re.sub(r' +', ' ', text)
    components = re.findall(r'продукт [а-я0-9., ]+изготовитель', text)
    amount = re.findall(r'количество перелитой [а-я0-9., ]+', text)
    trebovanie = re.findall(r'наименование среды [а-я0-9., ]+код среды', text)
    if len(components) > 0:
        w.write(a[1]+'\t'+a[3]+'\t'+a[4]+'\t'+a[10]+'\t'+components[0]+'\n')
    if len(amount) > 0:
        w.write(a[1]+'\t'+a[3]+'\t'+a[4]+'\t'+a[10]+'\t'+amount[0]+'\n')
    if len(trebovanie) > 0:
        w.write(a[1]+'\t'+a[3]+'\t'+a[4]+'\t'+a[10]+'\t'+trebovanie[0]+'\n')
w.close()
f.close()