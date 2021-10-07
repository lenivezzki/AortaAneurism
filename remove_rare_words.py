r = open('tomsk_almazov ЛКА_LEMME_no_stopwords.txt', 'r')
w = open('tomsk_almazov ЛКА_LEMME_no_stopwords_no_rarewords.txt', 'w')

def get_stopwords(filename, min):
    f = open(filename, 'r')
    arr = []
    for word in f.readlines():
        a = word.split('\t')
        if int(a[0]) <= min:
            w = a[1][:-1]
            arr.append(w)
    f.close()
    return arr

stopwords = get_stopwords('tomsk_almazov frec_dict 5st_step.txt', 2)

for line in r.readlines():
    a = line.split('\t')
    text = a[1][:-1]
    text = text.lower()
    words = text.split()
    new_words = [w for w in words if not w in stopwords]
    text = ' '.join(new_words)
    w.write(a[0] + '\t'+text +'\n')

r.close()
w.close()