def can_place(solution, x, y):
    if x not in solution:
        for f in solution:
            if f + (y - solution.index(f)) == x or f - (y - solution.index(f)) == x:
                return False
        return True
    else:
        return False
def print_res(res):
    row = "⬜⬛⬜⬛⬜⬛⬜⬛"
    for i in res:
        row_ready =row[:i] + "👑" + row[i + 1:]
        print(row_ready)
        row = row[-1] + row[:-1]
    print()
def main(x,res,r,delka):
    if can_place(res, x, len(res)):
        res.append(x)
        if len(res) >= delka:
            print_res(res)
            r += 1
            res.pop()
            x += 1
        else:
            x = 0
            x,res,r = main(x,res,r,delka)
    return x,res,r

def find_solutions(delka):
    x, r, res =0,0,[]
    while True:
        x, res, r = main(x, res, r, delka)
        while x >= delka - 1:
            if len(res) == 0:
                return r, res
            x = int(res[len(res) - 1])
            res.pop()
        x += 1
r, res = find_solutions(int(input()))
print(r)
