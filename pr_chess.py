

"""
Square A1 = (1,1)
Square B1 = (2,1)
Square D7 = (4,7)
"""


##################################  MAP A-H TO NUMBERS:
num_2_lett = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E", 
    6: "F", 
    7: "G", 
    8: "H"
    }
    
##################################  CREATE AN EMPTY BOARD:
board = {}

for AtoH in range(1,9):
    for Oneto8 in range(1,9):
        board[AtoH,  Oneto8] = None
        
print(f"\nempty board = {board}")

##################################  ADD PIECES FOR STARTING ARRANGEMENT:

for AtoH in range(1,9):
    board[AtoH,2] = "wp"
    board[AtoH,7] = "bp"

board[1,1] = "wr"
board[2,1] = "wkni"
board[3,1] = "wb"
board[4,1] = "wq"
board[5,1] = "wking"
board[6,1] = "wb"
board[7,1] = "wkni"
board[8,1] = "wr" 

board[1,8] = "br"
board[2,8] = "bkni"
board[3,8] = "bb"
board[4,8] = "bq"
board[5,8] = "bking"
board[6,8] = "bb"
board[7,8] = "bkni"
board[8,8] = "br" 

print(f"\nstarting board = {board}")


##################################  LIST ALL SQUARES WITH PIECES / PAWNS: 
squares_with_pieces = []
for square in board:
    if board[square] is not None:
        squares_with_pieces.append(square)
print(f"\nsquares_with_pieces = {squares_with_pieces}")

print(f"\nThe number of squares with pieces = {len(squares_with_pieces)}")

##################################  FIND ALL LEGAL MOVES: 

def pawn_legal_moves(square):

    print("\nPrint statements within function:")
    print(f"square = {square}")
    print(f"board[square] = {board[square]}")

    if board[square][0] == "w":
        colour = "white"
    elif board[square][0] == "b":
        colour = "black"
    else:
        raise Exception("Neither white nor black, this is unexpected")
    
    print(f"colour = {colour}\n")
    
    legal_moves = []



    ############################ WHITE:
    ############################ STRAIGHT AHEAD MOVES:
    if colour == "white":
        if board[ (square[0], square[1]+1 )  ] is None: 
            legal_moves.append( (square[0], square[1]+1 ) )
            if square[1] == 2:
                if board[ (square[0], square[1]+2 )  ] is None:
                    legal_moves.append( (square[0], square[1]+2 ) )
                    
        ############################ diagonal captures for white pawn:
        if square[0] >= 2:      # I.E. NOT COLUMN 'A'
            if board[square[0]-1, square[1]+1] is not None:
                if board[square[0]-1, square[1]+1][0] is "b":
                    legal_moves.append(  (square[0]-1, square[1]+1)  ) 
        if square[0] <= 7:       # I.E. NOT COLUMN 'H'
            if board[square[0]+1, square[1]+1] is not None:
                if board[square[0]+1, square[1]+1][0] is "b":
                    legal_moves.append(  (square[0]+1, square[1]+1 )  ) 

    ############################ black:
    ############################ STRAIGHT AHEAD MOVES:
    if colour == "black":
        if board[ (square[0], square[1]-1 )  ] is None: 
            legal_moves.append( (square[0], square[1]-1 ) )
            if square[1] == 7:
                if board[ (square[0], square[1]-2 )  ] is None:
                    legal_moves.append( (square[0], square[1]-2 ) )
        ############################ diagonal captures:
        if square[0] >= 2:       # I.E. NOT COLUMN 'A'
            if board[square[0]-1, square[1]-1] is not None:
                if board[square[0]-1, square[1]-1][0] is "w":
                    legal_moves.append(  (square[0]-1, square[1]-1)  ) 
        if square[0] <= 7:       # I.E. NOT COLUMN 'H'
            if board[square[0]+1, square[1]-1] is not None:
                if board[square[0]+1, square[1]-1][0] is "w":
                    legal_moves.append(  (square[0]+1, square[1]-1)  ) 
    return legal_moves
    
board[6,6] = "wp" 
print(f"***\nlegal moves for white pawn at f6 = {    pawn_legal_moves(  (6,6)  )    }\n***") 
print(f"***\nlegal_moves for white pawn at b2 = {    pawn_legal_moves((2,2))   }\n***")

board[6,3] = "bp" 
print(f"***\nlegal moves for black pawn at d7 = {    pawn_legal_moves(  (4,7)  )    }\n***") 
print(f"***\nlegal_moves for black pawn at f3 = {    pawn_legal_moves((6,3))   }\n***")

def rook_legal_moves(square): 

    print(f"square = {square}")
    print(f"board[square] = {board[square]}")

    if board[square][0] == "w":
        colour = "white"
    elif board[square][0] == "b":
        colour = "black"
    else:
        raise Exception("Neither white nor black, this is unexpected")
    
    print(f"colour = {colour}")
    
    legal_moves = []

    """
    ############################ STRAIGHT AHEAD MOVES:
    if colour == "white":

    4 directions
    """

    
    legal_moves = []
    return legal_moves

def bishop_legal_moves(square): 
    legal_moves = []
    return legal_moves
  
def queen_legal_moves(square): 
    legal_moves = []
    return legal_moves
    
def queen_legal_moves(square): 
    legal_moves = []
    return legal_moves


##################################  ASSERT IF CHECKMATE: 

##################################  ASSERT IF STALEMATE: 

