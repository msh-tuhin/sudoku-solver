import csv
import os
import new_utils
from sklearn.linear_model import SGDClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from sklearn.model_selection import cross_validate
from sklearn.model_selection import GridSearchCV

train_path = "../resource/lib/publicdata/aclImdb/train/"  # use terminal to ls files under this directory
test_path = "../resource/asnlib/public/imdb_te.csv"  # test data for grade evaluation

def imdb_data_preprocess(inpath, outpath="./", name="imdb_tr.csv", mix=False):
    pos = os.path.join(inpath, "pos")
    neg = os.path.join(inpath, "neg")
    file = open(os.path.join(outpath, name), "w", newline='')
    writer = csv.writer(file)

    writer.writerow(['row_number', 'text', 'polarity'])
    row_num = 0
    for pos_file, neg_file in zip(os.listdir(pos), os.listdir(neg)):
        file1 = open(os.path.join(pos, pos_file), "r")
        file2 = open(os.path.join(neg, neg_file), "r")
        text = file1.readline()
        l = text.split('<br />')
        text = ''.join(l)
        row_num += 1
        writer.writerow([row_num, text, 1])
        text = file2.readline()
        l = text.split('<br />')
        text = ''.join(l)
        row_num += 1
        writer.writerow([row_num, text, 0])
        file1.close()
        file2.close()

    file.close()


if __name__ == "__main__":
    imdb_data_preprocess(train_path)
    stopwords = []
    new_utils.just_stopwords(stopwords, "./stopwords.en.txt")
    corpus = []
    labels = []
    new_utils.create_corpus("./imdb_tr.csv", corpus, labels)

    vect = CountVectorizer(stop_words=stopwords)
    x = vect.fit_transform(corpus)
    vocab = vect.get_feature_names()
    # print(len(vocab))

    sgd = SGDClassifier()
    # clf.fit(x, labels)
    # cross_validate(clf, x, labels, cv=5)
    clf = GridSearchCV(sgd, [{'penalty': ["l1"], 'loss': ['hinge']}], cv=5)
    clf.fit(x, labels)

    test_file = open(test_path, "r", encoding="ISO-8859-1")
    reader = csv.reader(test_file)
    test_corpus = []

    for row in reader:
        break
    for row in reader:
        test_corpus.append(row[1])

    test_file.close()
    outfile = open("unigram.output.txt", "w")
    test_vect = CountVectorizer(stop_words=stopwords, vocabulary=vocab)
    test_x = test_vect.fit_transform(test_corpus)
    ans = clf.predict(test_x)
    for i in ans:
        outfile.write(i)
        outfile.write("\n")

    outfile.close()

    vect = CountVectorizer(stop_words=stopwords, ngram_range=(1, 2))
    x = vect.fit_transform(corpus)
    vocab = vect.get_feature_names()
    # print(len(vocab))

    sgd = SGDClassifier()
    # clf.fit(x, labels)
    # cross_validate(clf, x, labels, cv=5)
    clf = GridSearchCV(sgd, [{'penalty': ["l1"], 'loss': ['hinge']}], cv=5)
    clf.fit(x, labels)

    test_file = open(test_path, "r", encoding="ISO-8859-1")
    reader = csv.reader(test_file)
    test_corpus = []

    for row in reader:
        break
    for row in reader:
        test_corpus.append(row[1])

    test_file.close()
    outfile = open("bigram.output.txt", "w")
    test_vect = CountVectorizer(stop_words=stopwords, vocabulary=vocab, ngram_range=(1, 2))
    test_x = test_vect.fit_transform(test_corpus)
    ans = clf.predict(test_x)
    for i in ans:
        outfile.write(i)
        outfile.write("\n")

    outfile.close()

    vect = TfidfVectorizer(stop_words=stopwords)
    x = vect.fit_transform(corpus)
    vocab = vect.get_feature_names()
    # print(len(vocab))

    sgd = SGDClassifier()
    # clf.fit(x, labels)
    # cross_validate(clf, x, labels, cv=5)
    clf = GridSearchCV(sgd, [{'penalty': ["l1"], 'loss': ['hinge']}], cv=5)
    clf.fit(x, labels)

    test_file = open(test_path, "r", encoding="ISO-8859-1")
    reader = csv.reader(test_file)
    test_corpus = []

    for row in reader:
        break
    for row in reader:
        test_corpus.append(row[1])

    test_file.close()
    outfile = open("unigramtfidf.output.txt", "w")
    test_vect = TfidfVectorizer(stop_words=stopwords, vocabulary=vocab)
    test_x = test_vect.fit_transform(test_corpus)
    ans = clf.predict(test_x)
    for i in ans:
        outfile.write(i)
        outfile.write("\n")

    outfile.close()

    vect = TfidfVectorizer(stop_words=stopwords, ngram_range=(1, 2))
    x = vect.fit_transform(corpus)
    vocab = vect.get_feature_names()
    # print(len(vocab))

    sgd = SGDClassifier()
    # clf.fit(x, labels)
    # cross_validate(clf, x, labels, cv=5)
    clf = GridSearchCV(sgd, [{'penalty': ["l1"], 'loss': ['hinge']}], cv=5)
    clf.fit(x, labels)

    test_file = open(test_path, "r", encoding="ISO-8859-1")
    reader = csv.reader(test_file)
    test_corpus = []

    for row in reader:
        break
    for row in reader:
        test_corpus.append(row[1])

    test_file.close()
    outfile = open("bigramtfidf.output.txt", "w")
    test_vect = TfidfVectorizer(stop_words=stopwords, vocabulary=vocab, ngram_range=(1, 2))
    test_x = test_vect.fit_transform(test_corpus)
    ans = clf.predict(test_x)
    for i in ans:
        outfile.write(i)
        outfile.write("\n")

    outfile.close()
