#поиск ключевых слов
"""
r = open('patients_with operations_dataset_clean.txt', 'r')
w = open('объем_кровопотери ключевые_слова.txt', 'w')


docs = ['ДНЕВНИК_НАБЛЮДЕНИЙ_В_РЕАНИМАЦИОННОМ_ОТДЕЛЕНИИ',
        'ДНЕВНИК',
        'ДНЕВНИК_ССХ',
        'ДНЕВНИК_ССХ3',
        'ДНЕВНИК_НАБЛЮДЕНИЙ_В_РЕАНИМАЦИОННОМ_ОТДЕЛЕНИИ_ПИТ№7',
        'ОСМОТР_ХИРУРГА',
        'ПЕРЕВОДНОЙ_ЭПИКРИЗ_ИЗ_РЕАНИМАЦИОННОГО_ОТДЕЛЕНИЯ']

for line in r.readlines():
    a = line.split('\t')
    if a[10] not in docs:
        continue
    text = a[11]
    text = text.lower()
    sentenses = text.split('.')
    for s in sentenses:
        if s.find('дренаж') != -1:
            w.write(a[1]+'\t'+a[3]+'\t'+a[4]+'\t'+a[10]+'\t'+s+'\n')
r.close()
w.close()
"""

"""
import re

r = open('объем_кровопотери ключевые_слова.txt', 'r')
w = open('объем_кровопотери ТОЛЬКО_ключевые_слова.txt', 'w')


docs = ['ДНЕВНИК_НАБЛЮДЕНИЙ_В_РЕАНИМАЦИОННОМ_ОТДЕЛЕНИИ',
        'ДНЕВНИК',
        'ДНЕВНИК_ССХ',
        'ДНЕВНИК_ССХ3',
        'ДНЕВНИК_НАБЛЮДЕНИЙ_В_РЕАНИМАЦИОННОМ_ОТДЕЛЕНИИ_ПИТ№7',
        'ОСМОТР_ХИРУРГА',
        'ПЕРЕВОДНОЙ_ЭПИКРИЗ_ИЗ_РЕАНИМАЦИОННОГО_ОТДЕЛЕНИЯ']

for line in r.readlines():
    a = line.split('\t')
    if a[4] == 'NONE\n':
        w.write(a[4])
        continue
    text = a[4]
    text = text.lower()
    text = text.replace('ml', 'мл')
    text = text.replace('в умеренном количестве', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('за прошедшие сутки выделилось около', '')
    text = text.replace('объемом до', '')
    text = text.replace(' до ', ' ')
    text = text.replace('за сутки', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('выделилось', '')
    text = text.replace(' содержимого ', ' ')
    text = re.sub(r' +', ' ', text)
    text = text.replace('за прошедшие сутки суммарное количество около', 'суммарно за период')
    text = text.replace('около', '')
    text = re.sub(r' +', ' ', text)
    res2 = re.findall(r'суммарно за период \d+', text)
    res3 = re.findall(r'дренаж..? ?-? ?\d+', text)
    res4 = re.findall(r'кровопотеря \d+', text)
    res5 = re.findall(r'\d+ м?л? ?[а-я-]+? отделяем', text)
    res7 = re.findall(r'геморрагическ...? отделяемо..? ?-? ?\d+ ?м?л?', text)
    res6 = re.findall(r'\d+ м?л? ? серр?озно', text)
    res8 = re.findall(r'дренаж..? ?с?у?м?м?а?р?н?о? ?\d+ ?м?л?', text)
    res9 = re.findall(r'дренажного \d+ ?м?л? отделяемого', text)
    w.write(str(res2)+'\t'+str(res3)+'\t'+str(res4)+'\t'+str(res5)+'\t'+str(res6)+'\t'+str(res7)+'\t'+str(res8)+'\t'+str(res9)+'\n')

r.close()
w.close()
"""

import re

r = open('объем_кровопотери ключевые_слова.txt', 'r')
w = open('объем_кровопотери тест.txt', 'w')


docs = ['ДНЕВНИК_НАБЛЮДЕНИЙ_В_РЕАНИМАЦИОННОМ_ОТДЕЛЕНИИ',
        'ДНЕВНИК',
        'ДНЕВНИК_ССХ',
        'ДНЕВНИК_ССХ3',
        'ДНЕВНИК_НАБЛЮДЕНИЙ_В_РЕАНИМАЦИОННОМ_ОТДЕЛЕНИИ_ПИТ№7',
        'ОСМОТР_ХИРУРГА',
        'ПЕРЕВОДНОЙ_ЭПИКРИЗ_ИЗ_РЕАНИМАЦИОННОГО_ОТДЕЛЕНИЯ']

for line in r.readlines():
    a = line.split('\t')
    if a[4] == 'NONE\n':
        #w.write(a[4])
        continue
    text = a[4]
    text = text.lower()
    text = text.replace('ml', 'мл')
    text = text.replace('в умеренном количестве', '')
    text = text.replace('дренажи функционируют по системе наблюдается поступление содержимого в количестве', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('за прошедшие сутки выделилось около', '')
    text = text.replace('объемом до', '')
    text = text.replace(' до ', ' ')
    text = text.replace('за сутки', '')
    text = re.sub(r' +', ' ', text)
    text = text.replace('выделилось', '')
    text = text.replace(' содержимого ', ' ')
    text = re.sub(r' +', ' ', text)
    text = text.replace('за прошедшие сутки суммарное количество около', 'суммарно за период')
    text = text.replace('около', '')
    text = text.replace('дренажи функционируют', 'дренажу')
    text = re.sub(r' +', ' ', text)
    res2 = re.findall(r'суммарно за период \d+', text)
    res3 = re.findall(r'дренаж..? ?-? ?\d+', text)
    res4 = re.findall(r'кровопотеря \d+', text)
    res5 = re.findall(r'\d+ м?л? ?[а-я-]+? отделяем', text)
    res7 = re.findall(r'геморрагическ...? отделяемо..? ?-? ?\d+ ?м?л?', text)
    res6 = re.findall(r'\d+ м?л? ? серр?озно', text)
    res8 = re.findall(r'дренаж..? ?с?у?м?м?а?р?н?о? ?\d+ ?м?л?', text)
    res9 = re.findall(r'дренажного \d+ ?м?л? отделяемого', text)

    res = ''
    if len(res2) > 0:
        res = re.sub(r'[^0-9]+', '', res2[0])
    if len(res3) > 0:
        res = re.sub(r'[^0-9]+', '', res3 [0])
    if len(res4) > 0:
        res = re.sub(r'[^0-9]+', '', res4 [0])
    if len(res5) > 0:
        res = re.sub(r'[^0-9]+', '', res5 [0])
    if len(res6) > 0:
        res = re.sub(r'[^0-9]+', '', res6 [0])
    if len(res7) > 0:
        res = re.sub(r'[^0-9]+', '', res7 [0])
    if len(res8) > 0:
        res = re.sub(r'[^0-9]+', '', res8 [0])
    if len(res9) > 0:
        res = re.sub(r'[^0-9]+', '', res9[0])

    if res != '':
        w.write('\t'.join(a[:-1]) + '\t'+res+'\n')

r.close()
w.close()
""""""