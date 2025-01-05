# OOP-project-Python-Build-Tic-Tac-Toe-
oop


  ## description this project 
  
    this project consists of four class 

    
  class player:this class content of 2 atrrbuite (name,symbol) and 2 methods

  
  1- method chosse_name() ===> this method to get name from user and put it in name atrribute

  
  2- methods choose_symbol ====> this methods to get symbol from user and put it in symbol attribute 


class menu ===> this class content 3 methods 
1-method display_start_menu()===> this method display menu to chooice  start game or quit game 


2-method display_end_game()====> this methods display menu to chooice restart game or end the game 

3- method validition_choose() ===> this method check if chooice true or false and return chooice 

class board ===> this class content 1 attribute and 4 methods 

attribute board ===> this attribute it is about list start index from 0 to 9

1- method display _board()===>Displays the current state of the board in a user-friendly format.
Divides the board into rows and separates them with a horizontal line.


2- method update_board(chooice, symbol )===> pdates the board with the player's symbol if the chosen position is valid.
Parameters:

chooice: An integer representing the position on the board (1-9).

symbol: A string representing the player's symbol (e.g., "X" or "O").

Returns True if the move is valid and the board is updated; otherwise, returns False. 


3-methods is_valid_movied()===>Checks if the selected position is valid for a move.
Returns True if the position is still numeric (not occupied by a player's symbol); otherwise, False.


4- method restart()====> Resets the board to its initial state (numbers 1 through 9).
Uses the same list comprehension as in the constructor to recreate the board.

class game ===> in this class 3 another class composite to this class ,this class content from 4 atrributes and 8 methods 

Attributes

1-self.player:A list of two player objects, representing Player 1 and Player 2.
Each player object contains the player's name and symbol (e.g., "X" or "O").

2-self.board:An instance of the board class, representing the Tic-Tac-Toe game board.

3-self.menu:An instance of the menu class, which handles displaying menus and user choices.


4-self.index_player:An integer (0 or 1) that keeps track of whose turn it is.
Alternates between 0 (Player 1) and 1 (Player 2).

Methods


1. method start_game(self): Displays the main menu using menu.display_main_menu.

If the player chooses to start the game, it calls setup_player() to initialize player details.

If the player chooses to quit, it calls quit_game().

2- method  setup_player(self): Prompts both players to input their names and symbols.

Uses the player.choose_name() and player.choose_symbol() methods.

Clears the screen after each player's details are entered to improve user experience.

3- methods play_game(self): The main game loop. Runs until a player wins or the game ends in a draw.

Calls:

play_turn() for each player's move.

check_win() to determine if there's a winner.

check_draw() to determine if the board is full and no winner exists.

After the game ends, displays the endgame menu:

Option 1: Restart the game (restart_game()).

Option 2: Quit the game (quit_game()).


4- method play_turn(self): Handles a single player's turn:

Displays the current state of the board.

Prompts the current player to choose a position on the board.

Validates the move using board.update_board().

Switches to the other player after a valid move using switch_player().

5- method check_win(self): Checks for winning combinations (rows, columns, diagonals).
Returns True if any winning combination is found; otherwise, False.

6- method check_draw(self):Checks if all board positions are filled and no winner exists.
Returns True if it's a draw; otherwise, False.

7- method switch_player(self): Alternates the active player by toggling self.index_player between 0 and 1.

8-  restart_game(self): Resets the game by:

Restarting the board using board.restart().

Resetting the player index to 0.

Calling play_game() to start a new game.

9-  quit_game(self):  Prints a thank-you message and terminates the game.













