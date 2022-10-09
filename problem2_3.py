import utils
import csv
import sys
# in_file = "input2.csv"
# out_file = open("output2.csv", 'w', newline='')

in_file = sys.argv[1]
out_file = open(sys.argv[2], 'w', newline='')

examples = list()
utils.create_list_float(in_file, examples)
# print(examples)
# print(len(examples))
utils.scale(examples)
# print(examples)

writer = csv.writer(out_file)
# utils.grad_descent(0.1, examples, writer)
alphas = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 0.1010101]
for alpha in alphas:
    b0, b1, b2 = utils.grad_descent(alpha, examples, writer)
    writer.writerow([alpha, 100, b0, b1, b2])



out_file.close()

