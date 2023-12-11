#Sadri Ozgul - Tetris for the web
#Credit : Programming With Nick
#https://www.youtube.com/watch?v=nF_crEtmpBo
#CPSC-20000 Class Project Proposal 2023
class Colors:
    dark_grey = (26, 31, 40)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    light_blue = (59, 85, 162)
    Dark_gray = (99, 99, 99)
    light_gray = (179,179,179)
    
    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
