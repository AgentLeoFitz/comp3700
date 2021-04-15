class tictactoe(game):
    def __init__(self):
        super.__init__("TicTacToe","casual")
        global board = [['','',''],['','',''],['','','']]
    
    def start(self):
        global currentPlayer = players[0]
        global icon = 'x'
        self.showBoard()
        
    def move(self):
        move = input(currentPlayer.getName() + "move: ")
        rc = move.split(",")
        row = int(rc[0].trim())
        col = int(rc[1].trim())
        while (row > 2 or col > 2 or row < 0 or col < 0):
            print("OUT OF BOUNDS")
            move = input(currentPlayer.getName() + "move: ")
            rc = move.split(",")
            row = int(rc[0].trim())
            col = int(rc[1].trim())
        if board[r][c] == '':
            global board[r][c] = icon
        else:
            print("TAKEN")
            move = input(currentPlayer.getName() + "move: ")
            rc = move.split(",")
            row = int(rc[0].trim())
            col = int(rc[1].trim())

        if icon == 'x':
            global icon = 'o'
        else:
            global icon = 'x'
            
        
