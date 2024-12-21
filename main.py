import pygame
import math 
import random
from ai import AI


pygame.init()
pygame.font.init()

WIDTH = 450
HEIGHT = 450


running = True

BACKGROUND_COLOUR = (224, 198, 153)
BLACK = (0, 0, 0)
red = (200, 0, 0)
blue = (0, 0, 200)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")


class TicTacToe():
    def __init__(self, screen):
        self.screen = screen
        self.turn = 0
        self.board = [[-1]*3 for i in range(3)]
        self.winner = -1
        self.grid_width = 3
        self.circle_radius = 50
        self.circle_width = 15 
    
    def draw_board(self):
        for i in range(2):
            x = (i+1)*WIDTH // 3
            y = (i+1)*HEIGHT // 3
            pygame.draw.line(self.screen, BLACK, (x, 0), (x, HEIGHT), width=self.grid_width)
            pygame.draw.line(self.screen, BLACK, (0, y), (WIDTH, y), width=self.grid_width)
            
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == -1: continue
                x = j*WIDTH//3 + WIDTH//6
                y = i*HEIGHT//3 + HEIGHT//6
                if self.board[i][j] == 1:
                    f = pygame.font.SysFont('Comic Sans MS', 120)
                    text_surface = f.render('X', False, red)
                    text_rect = text_surface.get_rect()
                    text_rect.center = (x,y)
                    self.screen.blit(text_surface, text_rect)
                else:
                    pygame.draw.circle(self.screen, blue, (x,y), self.circle_radius, width=self.circle_width)
        
        if self.winner != -1:
            f = pygame.font.SysFont('Comic Sans MS', 50)    
            winning_colour = "blue"
            if self.winner == 2:
                text_surface = f.render("Tie!", False, BLACK)    
            else:
                if self.winner == 1: winning_colour = "red"
                text_surface = f.render(winning_colour + " has won!", False, BLACK)
                
            text_rect = text_surface.get_rect()
            text_rect.center = (WIDTH//2, HEIGHT//2)
            pygame.draw.rect(self.screen, BACKGROUND_COLOUR, text_rect)
            self.screen.blit(text_surface, text_rect)           

    def check_win(self, board):
        turn = 0
        for _ in range(2):
            for i in range(3):
                row = 0
                col = 0
                for j in range(3):
                    if board[i][j] == turn: col += 1
                    if board[j][i] == turn: row += 1

                if max(row,col) == 3:
                    return turn
            
            diag1 = 0
            diag2 = 0
            for i in range(3):
                if board[i][i] == turn: diag1 += 1
                if board[i][2-i] == turn: diag2 += 1
            
            if max(diag1, diag2) == 3:
                return turn
            
            turn = 1-turn
            
        if sum(self.board[i].count(-1) for i in range(3)) == 0:
            return 2        
        return -1
        
    def check_click(self,mouse_pos):
        if self.winner != -1: return 
        col = mouse_pos[0] // (WIDTH//3)
        row = mouse_pos[1] // (HEIGHT//3)
        if self.board[row][col] == -1:
            self.board[row][col] = self.turn
            self.winner = self.check_win(self.board)
            self.turn = 1 - self.turn
    
   
TTT = TicTacToe(screen)
my_AI = AI(TTT)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if (event.button == 1):
                TTT.check_click(pygame.mouse.get_pos())
                my_AI.get_best_move()
                                       
    screen.fill(BACKGROUND_COLOUR) 
    TTT.draw_board()

    pygame.display.flip()

pygame.quit()