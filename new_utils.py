def refine(text, res):
    import re
    for i in res:
        text = re.sub(i, '', text)
    return text


def get_stopwords(stopwords, filename, res):
    import re
    file = open(filename, "r")
    while True:
        line = file.readline()
        if line:
            line = line[:len(line) - 1]
            stopwords.append(line)
        else:
            break
    file.close()

    for word in stopwords:
        res.append(re.compile("\\b" + word + "\\b", flags=re.IGNORECASE))


def just_stopwords(stopwords, filename):
    file = open(filename, "r")
    while True:
        line = file.readline()
        if line:
            line = line[:len(line) - 1]
            stopwords.append(line)
        else:
            break
    file.close()


def create_corpus(filename, corpus, labels):
    import csv
    file = open(filename, "r")
    reader = csv.reader(file)
    i = 1
    for row in reader:
        break
    for row in reader:
        # if i == 1:
        #     i += 1
        #     continue

        # print(row[1])
        corpus.append(row[1])
        labels.append(row[2])
    file.close()





