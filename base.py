import utils
import csv
import sys


file = sys.argv[1]
file2 = open(sys.argv[2], "w", newline='')
writer = csv.writer(file2)

examples = list()
utils.create_list(file, examples)


b, w1, w2 = 0, 0, 0
while True:
    convergence = True
    for example in examples:
        f = utils.get_sign(example, b, w1, w2)
        if example[2] * f <= 0:
            convergence = False
            b = b + example[2]*1
            w1 = w1 + example[2] * example[0]
            w2 = w2 + example[2] * example[1]
    writer.writerow([w1, w2, b])
    if convergence:
        break
file2.close()















