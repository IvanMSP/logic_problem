
def grid(n: int, m: int) -> str:
    rows = n
    columns = m
    if rows == columns and rows > 1:
        if rows % 2 == 0:
            return 'L'
        else:
            return 'R'
    elif rows > columns and columns > 1:
        if columns % 2 == 0:
            return 'U'
        else:
            return 'D'
    elif columns > rows:
        if rows % 2 == 0:
            return 'L'
        else:
            return 'R'
    elif columns == 1:
        if rows == 1:
            return 'R'
        else:
            return 'D'


cases = int(input('Ingresa los test cases: '))
results = []

for c in range(0, cases):
    n = int(input('\nn: '))
    m = int(input('m: '))
    result = grid(n, m)
    results.append(result)

print([r for r in results])
