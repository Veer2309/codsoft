# TIC-TAC-TOE AI Implement an AI agent that plays the classic game of Tic-Tac-Toe against a human player. You can use algorithms like Minimax with or without Alpha-Beta Pruning to make the AI player unbeatable. This project will help you understand game theory and basic search algorithms.

import math

class TicTacToe:
    def _init_(self):
        self.board = [' ' for _ in range(9)]  # Initialize empty board
        self.current_player = 'X'  # Player 'X' starts first
    
    def print_board(self):
        for i in range(0, 9, 3):
            print(self.board[i:i+3])
    
    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == ' ']
    
    def make_move(self, position):
        self.board[position] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def undo_move(self, position):
        self.board[position] = ' '
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self, board=None):
        board = board or self.board
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
                return board[line[0]]
        if ' ' not in board:
            return 'draw'
        return None
    
    def minimax(self, depth, alpha, beta, is_maximizing):
        winner = self.check_winner()
        if winner == 'X':
            return -1
        elif winner == 'O':
            return 1
        elif winner == 'draw':
            return 0
        
        if is_maximizing:
            max_eval = -math.inf
            for move in self.available_moves():
                self.make_move(move)
                eval = self.minimax(depth + 1, alpha, beta, False)
                self.undo_move(move)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for move in self.available_moves():
                self.make_move(move)
                eval = self.minimax(depth + 1, alpha, beta, True)
                self.undo_move(move)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval
    
    def find_best_move(self):
        best_eval = -math.inf
        best_move = None
        for move in self.available_moves():
            self.make_move(move)
            eval = self.minimax(0, -math.inf, math.inf, False)
            self.undo_move(move)
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move
    
    def play(self):
        while True:
            self.print_board()
            
            # Human player's turn
            if self.current_player == 'X':
                human_move = int(input('Enter your move (0-8): '))
                self.make_move(human_move)
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    if winner == 'draw':
                        print("It's a draw!")
                    else:
                        print(f'Congratulations! {winner} wins!')
                    break
            
            # AI player's turn
            else:
                print('AI is thinking...')
                ai_move = self.find_best_move()
                self.make_move(ai_move)
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    if winner == 'draw':
                        print("It's a draw!")
                    else:
                        print(f'AI wins!')
                    break

# Start the game

if _name_ == '_main_':
    game = TicTacToe()
    game.play()