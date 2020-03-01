class SnakesLadders():

    def __init__(self, p1_position=0, p2_position=0, p1_turn=True, player_has_won=False):
        self.p1_position = p1_position
        self.p2_position = p2_position
        self.p1_turn = p1_turn
        self.player_has_won = player_has_won

    def __repr__(self):
        if self.p1_turn:
            turn = "player 1"
        else:
            turn = "player 2"

        return f'''Turn: {turn}
Player 1 is on square {self.p1_position}
player 2 is on square {self.p2_position}'''

    def play(self, die1, die2):

        board = {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 36: 44, 28: 84, 51: 67, 78: 98, 87: 94, 71: 91,
                 16: 6, 49: 11, 46: 25, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}

        def rules(player_position):
            landing = player_position + die1 + die2

            if landing == 100:
                self.player_has_won = True

            if die1 != die2:
                self.p1_turn = not self.p1_turn

            if landing > 100:
                landing = 200 - landing

            if landing in board.keys():
                landing = board[landing]
            return landing

        if self.player_has_won:
            return "Game over!"

        else:
            if self.p1_turn:
                self.p1_position = rules(self.p1_position)
                if self.player_has_won:
                    return f'Player 1 Wins!'
                return f'Player 1 is on square {self.p1_position}'
            else:
                self.p2_position = rules(self.p2_position)
                if self.player_has_won:
                    return f'Player 2 Wins!'
                return f'Player 2 is on square {self.p2_position}'