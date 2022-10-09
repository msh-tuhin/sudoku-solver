import csv


def create_list(filename, listname):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in range(len(row)):
                row[i] = int(row[i])
            listname.append(row)


def test_type(listname):
    for row in listname:
        for col in row:
            print(type(col))

def get_sign(example, b, w1, w2):
    sum = b + w1 * example[0] + w2 * example[1]
    if sum > 0:
        return 1
    else:
        return -1


def plot(examples, b, w1, w2):
    import matplotlib.pyplot as p
    for example in examples:
        if example[2] == -1:
            m = 'ro'
        else:
            m = 'bo'
        p.plot(example[0], example[1], m)
    p.show()


def create_list_float(filename, listname):
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            for i in range(len(row)):
                row[i] = float(row[i])
            # row.insert(0, 1)
            listname.append(row)


def scale(examples):
    import numpy
    f1 = list()
    f2 = list()
    for example in examples:
        f1.append(example[1])
        f2.append(example[2])
    # print(len(f1))
    # print(len(f2))
    stddev1 = numpy.std(f1)
    mean1 = numpy.mean(f1)
    stddev2 = numpy.std(f2)
    mean2 = numpy.mean(f2)
    # print("stddev1:", stddev1)
    # print("stddev2:", stddev2)
    for example in examples:
        example[1] = (example[1] - mean1)/stddev1
        example[2] = (example[2] - mean2)/stddev2


def grad_descent(alpha, examples, writer):
    b0, b1, b2 = 0, 0, 0
    cost = 0
    for i in range(100):
        sum_b0 = 0
        sum_b1 = 0
        sum_b2 = 0
        cost = 0
        for example in examples:
            diff = b0*example[0] + b1*example[1] + b2*example[2] - example[3]
            sum_b0 += diff*example[0]
            sum_b1 += diff*example[1]
            sum_b2 += diff*example[2]
            cost += diff*diff

        n = len(examples)
        # print(n)
        # print(alpha)
        # print(alpha/n)
        b0 = b0 - (alpha*sum_b0)/n
        b1 = b1 - (alpha/n)*sum_b1
        b2 = b2 - (alpha/n)*sum_b2
        cost = cost/(2*n)
        # print(cost)
        # writer.writerow([b0, b1, b2])
    # print(cost)
    return b0, b1, b2


def check_ratio(train_label, test_label):
    total_1_train = 0
    total_0_train = 0
    total_1_test = 0
    total_0_test = 0
    for i in test_label:
        if i == 1:
            total_1_test += 1
        else:
            total_0_test += 1

    for i in train_label:
        if i == 1:
            total_1_train += 1
        else:
            total_0_train += 1

    return total_1_train / total_0_train, total_1_test / total_0_test


def separate_data_label(prim_data, data, label):
    for l in prim_data:
        temp_list = list()
        temp_list.append(l[0])
        temp_list.append(l[1])
        data.append(temp_list)
        label.append(l[2])


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







