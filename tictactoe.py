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
            
    def winCheck(self):
        # Check x
        for i in range(0,2):
            sum = 0
            col = [row[i] for row in board]
            for j in range(0,2)
                if col[j] == 'x'
                    sum += 1
                if sum == 3:
                    return 'x'
            row = board[i]
            for j in range(0,2)
                if row[j] == 'x'
                    sum += 1
                if sum == 3:
                    return 'x'
        # Check o
        for i in range(0,2):
            sum = 0
            col = [row[i] for row in board]
            for j in range(0,2)
                if col[j] == 'o'
                    sum += 1
                if sum == 3:
                    return 'o'
            row = board[i]
            for j in range(0,2)
                if row[j] == 'o'
                    sum += 1
                if sum == 3:
                    return 'o'
        if board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
            return 'x'
        if board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
            return 'x'
        if board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
            return 'o'
        if board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
            return 'o'
        return ''
