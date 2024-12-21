import copy

class AI():
    def __init__(self, TTT):
        self.TTT = TTT
        self.ai_turn = 1
        self.memo = {}
        
    def list_to_tuple(self, board):
        for i in range(3):
            board[i] = tuple(board[i])
        
        return tuple(board)
    
    def tuple_to_list(self, board):
        new_board = []
        for i in range(3):
            new_board.append(list(board[i]))
        
        return new_board
        
    def get_possible_moves(self, board):
        moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == -1:
                    moves.append((i,j))
                    
        return moves

    
    def get_score(self, board, turn):
        if board in self.memo: return self.memo[board]
        
        winner = self.TTT.check_win(board)
        if winner == self.ai_turn:
            self.memo[board] = (-1, (-1, -1))
            return self.memo[board]
        elif winner == 1 - self.ai_turn:
            self.memo[board] = (1, (-1, -1))
            return self.memo[board]
                
        moves = self.get_possible_moves(board)
        
        if len(moves) == 0:
            self.memo[board] = (0, (-1, -1))
            return self.memo[board]

        scores = []
        
        for move in moves:
            new_board = copy.deepcopy(self.tuple_to_list(board))
            new_board[move[0]][move[1]] = turn
            scores.append((self.get_score(self.list_to_tuple(new_board), 1-turn)[0], move))
            
        scores.sort()
        if turn == self.ai_turn:
            self.memo[board] = scores[0]
        else:
            self.memo[board] = scores[-1]
        
        return self.memo[board]
        
        
    def get_best_move(self):
        board = copy.deepcopy(self.TTT.board)  
        board_tuple = self.list_to_tuple(board)
        
        best_move = self.get_score(board_tuple, self.TTT.turn)
            
        if best_move[0] == -1:
            print("AI is winning")
        elif best_move[0] == 1:
            print("Player is winning")
        else:
            print("Drawing")
        
        print("Best move is", best_move[1])