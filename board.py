from piece import Piece ,King ,Knight ,Queen ,Rook ,Bishop ,Pawn

class Board:
    
    def __init__(self):
        self.board = self.create_board()
        self.setup_pieces()
    
    def create_board(self):
        """ have to create a 8x8 matrix for the representation of chess_board """
        chess_board = []
        for _ in range(8):
            chess_board.append([None] * 8)        
        
        return chess_board

    def setup_pieces(self):
        """
            our board should look like :-
            
            R Kn B Q Ki B Kn R
            P P  P P P  P P  P
            . .  . . .  . .  .
            . .  . . .  . .  .
            . .  . . .  . .  .
            . .  . . .  . .  .
            P P  P P P  P P  P
            R Kn B Q Ki B Kn R
            
            Where   R  = Rook
                    Kn = Knight
                    B  = Bishop
                    Q  = Queen
                    Ki = King
                    P  = Pawn
        """
        
        """ set up pawn """
        for col in range(8):
            self.board[1][col] = Pawn('white')
            self.board[6][col] = Pawn('black')
        
        piece_order = [Rook ,Knight ,Bishop ,Queen ,King ,Bishop ,Knight ,Rook]
        
        """ setting up black piece """
        for col ,piece in enumerate(piece_order):
            self.board[0][col] = piece('white')
        
        """ setting up white piece """
        for col ,piece in enumerate(piece_order):
            self.board[7][col] = piece('black')
        
    def print_board(self):
        """Prints a text-based representation of the board."""
        for row in self.board:
            print([piece.symbol() if piece else '.' for piece in row])


obj = Board()
obj.print_board()
