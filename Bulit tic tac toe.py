import os 
def clear_screen():
    os.system("cls")
class player:
    def __init__(self):
        self.name=" "
        self.symbol=" "
    
    def choose_name(self):
            while True:
                name=input("enter your name :")
                if name.isalpha():
                    self.name=name
                    break
                print("enter your name again:")
    def choose_symbol(self):
            while True:
                symobal=input("enter your symbol: ")
                if symobal.isalpha() and len(symobal)==1:
                    self.symbol=symobal
                    break
                print("enter your correct symbol: ")
                     

# player1=player()
# print(player1.choose_symbol())
class menu:
    def validate_choose(self):
            while True:
                choose=int(input("enter  your choose 1 or 2: "))
                if choose == 1 or choose==2:
                    return choose
                    break
                print("enter correct choose")
    def display_main_menu(self):
            print("welcom to in your game: ")
            print("1- start game")
            print("2-quit game")
            return self.validate_choose()
    def display_endgame_menu(self):
            print("welcom to in your game: ")
            print("1- restart game")
            print("2-quit game")
            return self.validate_choose()

# player1=menu()
# print(player1.display_main_menu())
class board:
        def __init__(self): 
            self.board=[str(i) for i in range(1,10)]# list comprehension
            # for i in range(1,10):
            #         self.board.append(str(i))
        def display_board(self):
            for i in range(0,9,3):
                    print(" | ".join(self.board[i:i+3]))
                    if i<9:
                        print("_"*10)
        def update_board(self, chooice, symbol):  
            if self.is_valid_movied(chooice):
                self.board[chooice-1]=symbol
                return True
            return False
        def is_valid_movied(self,chooice): #sold principles
            return self.board[chooice-1].isnumeric()
        def restart(self):
             self.board=[str(i) for i in range(1,10)]
class game:
    def __init__(self):
        self.player=[player(),player()]
        self.board=board()
        self.menu=menu()
        self.index_player=0
    def start_game(self):
        chooice=self.menu.display_main_menu()
        print(chooice)
        if chooice == 1:
            self.setup_player()
        else:
            self.quit_game()

    def setup_player(self):
        for index,player in enumerate(self.player,start=1):
            print(f"player {index} ,enter your detaills:  ")
            player.choose_name()
            player.choose_symbol()
            clear_screen()
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                chooice=self.menu.display_endgame_menu()
                if chooice==1:
                    self.restart_game()
                else:
                    self.quit_game()
                    break
    def play_turn(self):
        player =self.player[self.index_player]
        self.board.display_board()
        print(f" {player.name}’s turn {player.symbol} ")
        while True:
            try:
                    chooice=int(input("enter your numebr from about board: "))
                    if 1<= chooice <= 9 and self.board.update_board(chooice,player.symbol) :
                        break
                    else:
                        print("invalid move try agine: ")
            except ValueError:
                    print("enter correct chooice: ")
        clear_screen()
        self.switch_player()
        
    def check_win(self):
        win_combination=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for comb in win_combination:
            if(self.board.board[comb[0]] == self.board.board[comb[1]] == self.board.board[comb[2]]):
                     return True
        return False
    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)
    def switch_player(self):
        self.index_player=1-self.index_player
    def restart_game(self):
        self.board.restart()
        self.index_player=0
        self.play_game()
    def quit_game(self):
        print("thank you for playing")
play=game()
play.start_game()
play.play_game()
# print(play.board)








# player1=board()
# player1.display_board()