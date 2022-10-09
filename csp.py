import csp_util
import sys
import time


if __name__ == '__main__':
    start = time.time()
    # print(sys.getrecursionlimit())
    # sys.setrecursionlimit(4000)
    file = open("C:\\Users\\Tuhin\\Desktop\\sudoku_start.txt", "r")
    out = open("C:\\Users\\Tuhin\\Desktop\\out2.txt", "w")
    lines = file.readlines()
    count = 0
    for line in lines:
        neighbors = dict()
        csp_util.create_neighbors(neighbors)
        initial = line
        # initial = "000260701680070090190004500820100040004602900050003028009300074040050036703018000"
        initial = "800000000003600000070090200050007000000045700000100030001000068008500010090000400"
        sudoku = dict()
        csp_util.create_initial(sudoku, initial)
        domain = dict()
        csp_util.create_domain(domain, sudoku)

        flag = csp_util.ac3(neighbors, domain)
        if flag:
            if csp_util.check_completion(domain):
                text = ""
                for k in sorted(sudoku.keys()):
                    text += domain[k][0]
                out.write(text + " " + "AC3" + "\n")
            else:
                s = csp_util.bts(sudoku, domain, neighbors)
                text = ""
                for k in sorted(s.keys()):
                    text += s[k]
                out.write(text + " " + "BTS" + "\n")
        else:
            print("Inconsistent")
        break
        count += 1
        print(count)
    # print(count)
    out.close()
    end = time.time()
    print((end - start))




