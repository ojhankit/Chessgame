from piece import Piece ,Pawn ,Rook ,Bishop ,Queen ,King ,Knight
from board import Board

class Game:
    
    def __init__(self ,color):
        self.board = Board()
        self.current_color = color
        self.is_over = False
    
    def switch_turns(self):
        
        self.current_color = 'black' if self.current_color == "white" else "white"
        
    def play(self):
    
        while not self.is_over:
            self.board.print_board()
            print(f"{self.current_color.capitalize()} is playing")
            
            start_position = self.get_user_input("Enter the start position (row ,col)")
            end_position = self.get_user_input("Enter the end position (row ,col)")
            
            if self.board.move_pieces(start_position ,end_position ,self.current_color):
                self.switch_turns()
            
            else:
                print("Invalid move.. Please Take Another move")
            
            self.check_game_over()
    
    def get_user_input(self, prompt: str) -> tuple[int, int]:
        """take the input from user and convert to a tuple of integers."""
        while True:
            try:
                user_input = input(prompt)
                row, col = map(int, user_input.split(","))
                if 0 <= row < 8 and 0 <= col < 8:
                    return (row, col)
                else:
                    print("Invalid input.. Enter values between 0 and 7.")
            except ValueError:
                print("Invalid input format.. Use row,col format.")
    