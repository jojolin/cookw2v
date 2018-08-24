# coding:utf8
'''
Run in nlp env: `source activate nlp`
'''
import sys
from gensim.models import Word2Vec


def load_model(path):
    return Word2Vec.load(path)

def vec(modelfp, word):
    return load_model(modelfp).wv[word]

def similar(modelfp, word):
    wv = load_model(modelfp).wv
    return wv.most_similar(word)

def similar2(modelfp, positives, negtives):
    wv = load_model(modelfp).wv
    if negtives is None:
        print('no negtives.')
        result = wv.most_similar(positive=positives)
    else:
        print('has negtives.')
        result = wv.most_similar(positive=positives, negative=negtives)
    for x in result:
        print("{}: {:.4f}".format(*x))

    # result = wv.most_similar(positive=['woman', 'king'], negative=['man'])
    # print("{}: {:.4f}".format(*result[0]))
    # queen: 0.7699

    # result = wv.most_similar_cosmul(positive=['woman', 'king'], negative=['man'])
    # print("{}: {:.4f}".format(*result[0]))
    # queen: 0.8965

    # print(wv.doesnt_match("breakfast cereal dinner lunch".split()))

    # cereal
    # similarity = wv.similarity('woman', 'man')
    # similarity > 0.8
    # True

    # result = wv.similar_by_word("cat")
    # print("{}: {:.4f}".format(*result[0]))
    # dog: 0.8798

    # sentence_obama = 'Obama speaks to the media in Illinois'.lower().split()
    # sentence_president = 'The president greets the press in Chicago'.lower().split()
    # similarity = wv.wmdistance(sentence_obama, sentence_president)
    # print("{:.4f}".format(similarity))
    # 3.4893

    # distance = wv.distance("media", "media")
    # print("{:.1f}".format(distance))
    # 0.0

    # sim = wv.n_similarity(['sushi', 'shop'], ['japanese', 'restaurant'])
    # print("{:.4f}".format(sim))
    # 0.7067

    # vector = wv.word_vec('office', use_norm=True)
    # vector.shape
    # (100,)

def main():
    model_filep = sys.argv[2]
    word = sys.argv[3]
    if sys.argv[1] == 'vec':
        print('vec: {}'.format(vec(model_filep, word)))

    elif sys.argv[1] == 'simi':
        print('similars: {}'.format(similar(model_filep, word)))

    elif sys.argv[1] == 'simi2':
        positives = word.split(" ")
        print(len(sys.argv))
        negtives = sys.argv[4].split(" ") if len(sys.argv) > 4 else None
        print('get poss: %s, negs: %s' % (positives, negtives))
        similar2(model_filep, positives, negtives)

    else:
        print('Usage: tail -n 50 evalute.py')

if __name__ == '__main__':
    main()
