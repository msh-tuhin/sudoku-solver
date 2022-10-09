import csp_util
import sys

if __name__ == '__main__':
    out = open("output.txt", "w")
    count = 0
    neighbors = dict()
    csp_util.create_neighbors(neighbors)
    initial = sys.argv[1]
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
            out.write(text + " " + "AC3")
        else:
            s = csp_util.bts(sudoku, domain, neighbors)
            text = ""
            for k in sorted(s.keys()):
                text += s[k]
            out.write(text + " " + "BTS")
    out.close()




