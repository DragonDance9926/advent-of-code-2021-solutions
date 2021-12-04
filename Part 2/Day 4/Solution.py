

with open("input.txt") as file:
    bingo_numbers = list(map(int, next(file).split(",")))

    boards = []
    for row in file:
        row = row.strip()
        if row == "":
            board = []
            boards.append(board)
            continue
        board += map(int, row.split())

def wins(board:list) -> bool:
    for i in range(0, 5):
        if all(n < 0 for n in board[5 * i:5 * i + 5]):
            return True
        if all(n < 0 for n in board[i::5]):
            return True
    return False

def lwinner():
    for n in bingo_numbers:
        winners = []
        for i in range(len(boards)):
            boards[i] = [a if a != n else -1 for a in boards[i]]
            if wins(boards[i]):
                if len(boards) == 1:
                    return n*sum(x for x in boards[i] if x >= 0)
                winners.append(boards[i])
        for board in winners:
            boards.remove(board)
print(lwinner())