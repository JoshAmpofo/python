"""
Project: Learn Classes and Objects by building a sudoku puzzle solver
"""

# create Board class
class Board:
    # initialize board
    def __init__(self, board):
        self.board = board
    
    # create board outline using special charsets
    def __str__(self):
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines
        
        # create 3x3 grid within board
        for index, line in enumerate(self.board):
            row_list = []
            # 3x3 grid line
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                row_square = '|'.join(str(item) for item in part)
                row_list.extend(row_square)
                
                if square_no != 3:
                    row_list.append('║')
                    
            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace('0', ' ')
            board_string += row_empty
            
            # dealing with last row
            if index < 8:
                # verify row
                if index % 3 == 2:
                    # extend board string
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                # add middle borders
                else:
                    board_string += middle_lines
            # handle last row of board
            else:
                board_string += lower_lines
        
        # return complete board
        return board_string