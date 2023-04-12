

##################################  CREATE AN EMPTY BOARD:
board = {}

for r in range(1,9):
    for c in range(1,9):
        board[r,c] = None
        
print(f"\nempty board = {board}")

##################################  ADD PIECES FOR STARTING ARRANGEMENT:

for c in range(1,9):
    board[2,c] = "wp"
    board[7,c] = "bp"

board[1,1] = "wr"
board[1,2] = "wkni"
board[1,3] = "wb"
board[1,4] = "wq"
board[1,5] = "wking"
board[1,6] = "wb"
board[1,7] = "wkni"
board[1,8] = "wr" 

board[8,1] = "br"
board[8,2] = "bkni"
board[8,3] = "bb"
board[8,4] = "bq"
board[8,5] = "bking"
board[8,6] = "bb"
board[8,7] = "bkni"
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
    legal_moves = []
    return legal_moves
    
def rook_legal_moves(square): 
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

