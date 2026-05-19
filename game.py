import os


class Board:
    def __init__(self):
        self.board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|' + '|'.join(row) + '|')

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '_':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '_':
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '_':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '_':
            return self.board[0][2]
        return None


game = Board()
current_player = 'X'
while True:
    os.system('clear')
    game.display()
    try:
        row = int(input('Введите строку (1, 2, 3): ')) - 1
        col = int(input('Веедите столбец (1, 2, 3): ')) - 1
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print('Ошибка! Вводите числа от 1 до 3.')
            continue
    except ValueError:
        print('Ошибка! Нужно вводить только цифры. Попробуйте еще раз.')
        continue
    if game.board[row][col] == '_':
        game.make_move(row, col, current_player)
        print('\nХод принят!')
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    else:
        print('Эта клетка уже занята! Попробуй другую.')

    winner = game.check_winner()
    if winner:
        game.display()
        print(f'Ура! Победили {winner}!')
        break

    flat_board = []
    for row in game.board:
        flat_board.extend(row)

    if '_' not in flat_board:
        game.display()
        print('Ничья! Свободных клеток больше нет.')
        break

