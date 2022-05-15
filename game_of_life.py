from gc import get_count
from operator import ne
from pprint import pprint
from turtle import pen
import pygame
import random
from pygame.locals import *


class GameOfLife:
    
    def __init__(self, width = 640, height = 400, cell_size = 30, speed = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)

        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size


        self.speed = speed

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (0, y), (self.width, y))
    
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        clist = self.cell_list(True)
        # clist = self.cell_list(True)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            # self.draw_grid() 
            self.draw_cell_list(clist)
            pygame.display.flip()
            clist = self.update_cell_list(clist)
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize=False):
        res = [[random.choice((0,0,0,0,0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1)) for x in range(self.cell_width)] for y in range(self.cell_height)]
        return res

    def draw_cell_list(self, rects):
        for i, y in enumerate(rects):
            for j, x in enumerate(y):
                if x == 1:
                    pygame.draw.rect(self.screen, pygame.Color('black'), (j * self.cell_size, i * self.cell_size + 1, self.cell_size + 1, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), (j * self.cell_size, i * self.cell_size + 1, self.cell_size + 1, self.cell_size))

    def get_neighbours(self, cell):
        nei_list = []
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                x = cell[0] + i
                y = cell[1] + j
                if x < 0 or x >= self.cell_width or y < 0 or y >= self.cell_height:
                    continue
                if x == cell[0] and y == cell[1]:
                    continue
                one_nei = (x, y)
                nei_list.append(one_nei)
        return nei_list
    
    def get_count(self, cell, cell_list):
        neis = self.get_neighbours(cell)
        i = 0
        for n in neis:
            # try:
            #     if cell_list[n[1]][n[0]] == 1:
            #         i += 1
            # except:
            #     pass
            if cell_list[n[1]][n[0]] == 1:
                i += 1
        return i
    
    def update_cell_list(self, cell_list):
        for i, y in enumerate(cell_list):
            for j, x in enumerate(y):
                if x == 1:
                    if self.get_count((j, i), cell_list) not in (2, 3):
                        cell_list[i][j] = 0
                        continue
                    cell_list[i][j] = 1
                    continue
                if self.get_count((j, i), cell_list) == 3:
                    cell_list[i][j] = 1
                    continue
                cell_list[i][j] = 0
        return cell_list
                    

if __name__ == '__main__':
    game = GameOfLife(1920, 940, 10)
    game.run()
 