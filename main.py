import random

class Player:
    def __init__(self, name):
        self.name = name
        self.moves = list()

    def has_won(self, axes: list) -> bool:
        if len(self.moves) < 3: return False

        axe = set(self.moves)

        if axe in axes:
            return True

        return False



board = {
    'board':"""
    x1 | x2 | x3 
    ____ ____ ____

    y1 | y2 | y3 
    ____ ____ ____

    z1 | z2 | z3 
    """,

    'points':{
        (0, 0): 'x1',
        (0, 1): 'x2',
        (0, 2): 'x3',
        (1, 0): 'y1',
        (1, 1): 'y2',
        (1, 2): 'y3',
        (2, 0): 'z1',
        (2, 1): 'z2',
        (2, 2): 'z3'
    },
    'axes': [
        {(0, 0), (0, 1), (0, 2)}, 
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},
        {(0, 0), (1, 0), (2, 0)},
        {(1, 0), (1, 1), (1, 2)},
        {(2, 0), (2, 1), (2, 2)},
        {(0, 0), (1, 1), (2, 2)},
        {(0, 2), (1, 1), (2, 0)}    
    ]
}

# (row, col)
available_moves = [
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2)
]


computer_player = Player('computer')
user_player = Player('user')

play = True

while play:
    # Draw the boar
    # Replace user computer by Xs and Os
    # for move in user_player.moves:
    #     board['board'].replace(board['points'][move], 'X')

    # for move in computer_player.moves:
    #     board['board'].replace(board['points'][move], 'O')


    print(board['board'])

    print(available_moves)
    

    # Prompt user to enter a valid move
    str_move = input("Enter a move. Start with row then col: ")
    user_move = (int(str_move[0]), int(str_move[2]))

    if user_move in available_moves:
        user_player.moves.append(user_move)
        available_moves.remove(user_move)
    else:
        print("Invalid move")

    if user_player.has_won(board['axes']):
        print("You win 🏆")
        play = False
    else:
        if len(available_moves) > 0: 
            computer_move = random.choice(available_moves)
            computer_player.moves.append(computer_move)
            available_moves.remove(computer_move)

        if computer_player.has_won(board['axes']):
            print("Computer wins 🏆\nYou lose 😭")
            play = False

    if len(available_moves) == 0 and play:
        print("It's a draw 🫢")
        print(user_player.moves)
        print(computer_player.moves)
        play = False

