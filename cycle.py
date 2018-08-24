# coding: utf8
'''
Find the cycle of some topic
'''
import sys
from gensim.models import Word2Vec

TOPN_SIMILAR = 9
MINI_SIMILAR = 5

def load_model(path):
    model = Word2Vec.load(path)
    wv = model.wv
    del model
    return wv

def find_cycle(modelfp, word, num, prop):
    '''
    find cycle of a word.
    '''
    wv = load_model(modelfp)
    checked = []
    unchecked = []

    unchecked.append(word)
    while (len(checked) < num and len(unchecked) != 0):
        wd = unchecked.pop(0)
        if wd in checked:
            continue

        count_prop_simis = 0
        simis = []
        similars = wv.most_similar(wd, topn=TOPN_SIMILAR)
        for simi, prp in similars:
            if prp < prop:
                continue

            count_prop_simis += 1

            if simi in checked:
                continue
            else:
                simis.append(simi)

        # this means the word is around the edge of some type
        if count_prop_simis < MINI_SIMILAR:
            print('edge simi: %s' % wd)
            continue

        checked.append(wd)   # add to checked set
        unchecked.extend(simis)    # add to uncheck set

    print('remain len(unchecked): {}'.format(len(unchecked)))
    return checked

def main():
    model_filep = sys.argv[1]
    num = int(sys.argv[2])
    prop = float(sys.argv[3])
    word = sys.argv[4]
    cycle = find_cycle(model_filep, word, num, prop)
    print('cycle: {}'.format(cycle))


if __name__ == '__main__':
    main()
