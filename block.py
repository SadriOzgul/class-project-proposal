#Sadri Ozgul - Tetris for the web
#Credit : Programming With Nick
#https://www.youtube.com/watch?v=nF_crEtmpBo
#CPSC-20000 Class Project Proposal 2023
from colors import Colors
import pygame
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.roation_state = 0 
        self.colors = Colors.get_cell_colors()
    
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns
        
    def get_cell_positions(self):
        tiles = self.cells[self.roation_state]
        moved_tiles = []
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles
    
    def rotate(self):
        self.roation_state += 1
        if self.roation_state == len(self.cells):
            self.roation_state = 0
            
    def undo_rotation(self):
        self.roation_state -= 1
        if self.roation_state == 0:
            self.roation_state == len(self.cells) - 1
        
    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size, offset_y + tile.row * self.cell_size,
            self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)