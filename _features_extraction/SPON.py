f = open('patients_with operations_dataset_clean.txt', 'r')
w = open('СПОН.txt', 'w')

import re

def var1(text):
    return re.findall(r' спон ', text) #СПОН

for line in f.readlines():
    a = line.split('\t')
    text = ' ' + a[11] + ' '
    text = text.lower()
    text = re.sub(r'[^а-я0-9 ё]+', ' ', text)
    text = re.sub(r' +', ' ', text)
    text = text.replace('синдром полиогарнн', ' спон ')
    text = text.replace(' пон ', ' спон ')
    text = text.replace('полиогарнн', ' спон ')
    text = re.sub(r' +', ' ', text)
    text = text.replace('явлениями почечной недостаточности дыхательной недостаточности', 'спон')
    text = text.replace('явлениями сердечно сосудистой недостаточности дыхательной недостаточности', 'спон')
    text = text.replace('явлениями сердечно сосудистой недостаточности почечной недостаточности', 'спон')
    text = text.replace(' свр ', ' ')
    text = text.replace('вследствии пневмонии ', '')
    text = text.replace('явлениями ссн дн опн', 'спон')
    text = text.replace('явлениями ссн опн дн', 'спон')
    text = text.replace('явлениями дн ссн опн', 'спон')
    text = text.replace('явлениями дн опн ссн', 'спон')
    text = text.replace('явлениями опн ссн дн', 'спон')
    text = text.replace('явлениями опн дн ссн', 'спон')
    text = text.replace('явлениями ссн дн', 'спон')
    text = text.replace('явлениями ссн опн', 'спон')
    text = text.replace('явлениями дн ссн', 'спон')
    text = text.replace('явлениями дн опн', 'спон')
    text = text.replace('явлениями опн дн', 'спон')
    text = text.replace('явлениями опн ссн', 'спон')

    text = text.replace('тяжесть состояния обусловлена дн ссн', 'спон')
    text = text.replace('тяжесть состояния обусловлена ссн дн', 'спон')
    text = text.replace('тяжесть состояния обусловлена ссн опн', 'спон')
    text = text.replace('тяжесть состояния обусловлена дн опн', 'спон')
    text = text.replace('тяжесть состояния обусловлена опн дн', 'спон')
    text = text.replace('тяжесть состояния обусловлена опн ссн', 'спон')


    res = '0'

    res1 = var1(text)
    if len(res1) > 0:
        res = '1'
    if res != '0':
        w.write(a[1] + '\t' + a[3]+'\t' + a[10] + '\t' + res + '\n')


f.close()
w.close()