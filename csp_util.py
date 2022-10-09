import copy

boxes = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': ['E', 'F'],
    'E': ['D', 'F'],
    'F': ['D', 'E'],
    'G': ['H', 'I'],
    'H': ['G', 'I'],
    'I': ['G', 'H'],
    '1': ['2', '3'],
    '2': ['1', '3'],
    '3': ['1', '2'],
    '4': ['5', '6'],
    '5': ['4', '6'],
    '6': ['4', '5'],
    '7': ['8', '9'],
    '8': ['7', '9'],
    '9': ['7', '8']
}

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def create_neighbors(neighbors):
    for letter in letters:
        for num in nums:
            k = letter + num
            neighbors[k] = []
            for n in nums:
                if n != num:
                    neighbors[k].append(letter+n)
            for l in letters:
                if l != letter:
                    neighbors[k].append(l+num)
            for i in boxes[letter]:
                for j in boxes[num]:
                    neighbors[k].append(i+j)


def create_initial(sudoku, initial):
    for i in range(81):
        if i < 9:
            sudoku['A'+str(i+1)] = initial[i]
            continue
        if i < 18:
            sudoku['B'+str((i+1) - 9)] = initial[i]
            continue
        if i < 27:
            sudoku['C'+str((i+1) - 18)] = initial[i]
            continue
        if i < 36:
            sudoku['D'+str((i+1) - 27)] = initial[i]
            continue
        if i < 45:
            sudoku['E'+str((i+1) - 36)] = initial[i]
            continue
        if i < 54:
            sudoku['F'+str((i+1) - 45)] = initial[i]
            continue
        if i < 63:
            sudoku['G'+str((i+1) - 54)] = initial[i]
            continue
        if i < 72:
            sudoku['H'+str((i+1) - 63)] = initial[i]
            continue
        if i < 81:
            sudoku['I'+str((i+1) - 72)] = initial[i]
            continue


def create_domain(domain, sudoku):
    for k in sorted(sudoku.keys()):
        if sudoku[k] == '0':
            domain[k] = copy.copy(nums)
        else:
            domain[k] = list(sudoku[k])


def create_q(q, inque, neighbors):
    for k in sorted(neighbors.keys()):
        for n in neighbors[k]:
            q.append(k+n)
            inque[k+n] = 1


def revise(x, y, domain):
    revised = False
    dy = copy.copy(domain[y])
    if len(dy) == 1:
        # print(dy)
        # print(domain[x])
        if dy[0] in domain[x]:
            domain[x].remove(dy[0])
            revised = True
        # print(domain[x])
    return revised


def ac3(neighbors, domain):
    q = list()
    inque = dict()
    create_q(q, inque, neighbors)
    # print(len(q))
    while len(q) > 0:
        arc = q.pop()
        inque[arc] = 0
        x = arc[:2]
        y = arc[2:]
        if revise(x, y, domain):
            if len(domain[x]) == 0:
                return False
            for n in neighbors[x]:
                if n != y and inque[n+x] == 0:
                    q.insert(0, n+x)
                    inque[n+x] = 1
    return True


def check_completion(domain):
    for k in domain.keys():
        if len(domain[k]) > 1:
            return False
    return True


def select_var(sudoku, domain):
    var = ''
    for k in sudoku.keys():
        if sudoku[k] == '0':
            var = k
            break
    length = len(domain[var])
    for k in sudoku.keys():
        if sudoku[k] == '0':
            if len(domain[k]) < length:
                var = k
                length = len(domain[var])
    return var


def check_assign(var, value, sudoku, domain, neighbors):
    for n in neighbors[var]:
        if sudoku[n] != '0':
            if sudoku[n] == value:
                return False
        else:
            if value in domain[n]:
                # domain[n].remove(value)
                # if len(domain[n]) == 0:
                #     return False
                if len(domain[n]) == 1:
                    return False
                else:
                    domain[n].remove(value)
    return True


def bts(sudoku, domain, neighbors):
    return backtrack(copy.deepcopy(sudoku), copy.deepcopy(domain), neighbors)


def backtrack(sudoku, domain, neighbors):
    if check_completion(domain):
        for k in sudoku.keys():
            if sudoku[k] == '0':
                sudoku[k] = domain[k][0]
        return sudoku
    var = select_var(sudoku, domain)
    # print(var)
    # print(len(domain['A1']))
    dd = domain[var]
    for value in dd:
        temp = copy.deepcopy(domain)
        if check_assign(var, value, sudoku, domain, neighbors):
            sudoku[var] = value
            domain[var] = list(value)
            result = backtrack(copy.deepcopy(sudoku), copy.deepcopy(domain), neighbors)
            if result is not False:
                return result
            sudoku[var] = '0'
            domain = copy.deepcopy(temp)
    return False


