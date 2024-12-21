import copy

class AI():
    def __init__(self, TTT):
        self.TTT = TTT
        self.ai_turn = 1
        
    def get_possible_moves(self, board):
        moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == -1:
                    moves.append((i,j))
                    
        return moves
    
    def get_score(self, board, turn):
        winner = self.TTT.check_win(board)
        if winner == self.ai_turn:
            return -1
        elif winner == 1 - self.ai_turn:
            return 1
                
        moves = self.get_possible_moves(board)
        
        if len(moves) == 0:
            return 0

        scores = []
        
        for move in moves:
            new_board = copy.deepcopy(board)
            new_board[move[0]][move[1]] = turn
            scores.append(self.get_score(new_board, 1-turn))
            
        if turn == self.ai_turn:
            return min(scores)
        else:
            return max(scores)
        
        
    def get_best_move(self):
        board = copy.deepcopy(self.TTT.board)        
        moves = self.get_possible_moves(board)
        if len(moves) == 0:
            return (-1, (-1, -1))
        best_moves = []
        for move in moves:
            new_board = copy.deepcopy(board)
            new_board[move[0]][move[1]] = self.TTT.turn
            best_moves.append((self.get_score(new_board, 1-self.TTT.turn), move))
        
        best_moves.sort()
        if self.TTT.turn == self.ai_turn:
            move = best_moves[0]
        else:
            move = best_moves[-1]
            
        if move[0] == -1:
            print("AI is winning")
        elif move[0] == 1:
            print("Player is winning")
        else:
            print("Drawing")
        
        possible_moves = []
        for i in best_moves:
            if i[0] == move[0]: possible_moves.append(i[1])
            
        print("Best move is", possible_moves)