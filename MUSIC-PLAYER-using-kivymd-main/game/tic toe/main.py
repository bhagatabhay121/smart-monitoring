# This game was made for a example show off how to use kivymd
# make sure you run "pip install kivymd" before run the main.py file
# feel free to edit 
# greetings S3R43o3 © 2022
import kivy
from kivy.lang import Builder
from kivy.factory import Factory
from kivymd.app import MDApp
from kivy.utils import platform
from kivy.core.window import Window

defaultScreen = "layoutmain.kv"

class GameApp(MDApp):
    def build(self):
        # build the basic app and set colorthemes
        self.title = "Tic Tac Toe"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_file(defaultScreen)
    
    # define whos turn it is
    turn = "X"
    # track win or lose
    winner = False
    # track win count
    X_win = 0
    O_win = 0

    # handler for pressing the game buttons
    # it will change the turn to next player and colorize/disable the button
    def presser(self, btn):
        if self.turn == "X":
            btn.disabled_color = "red"
            btn.background_color = 1 , 0 , 0 , .2
            btn.text = "X"
            self.turn = "O"
            self.root.ids.score.color = "blue"
            self.root.ids.score.text = "O´s Turn!"
            btn.disabled = True
        else:
            btn.background_color = 0 , 0 , 1 , .2
            btn.text = "O"
            self.turn = "X"
            self.root.ids.score.color = "red"
            self.root.ids.score.text = "X´s Turn!"
            btn.disabled_color = "blue"
            btn.disabled = True

        self.win()


    # handler to check if a win is true
    def win(self):
       # Across
        if self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn2.text and self.root.ids.btn2.text == self.root.ids.btn3.text:
            return self.end_game(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)

        elif self.root.ids.btn4.text != "" and self.root.ids.btn4.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn6.text:
            return self.end_game(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)

        elif self.root.ids.btn7.text != "" and self.root.ids.btn7.text == self.root.ids.btn8.text and self.root.ids.btn8.text == self.root.ids.btn9.text:
            return self.end_game(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)

        # Down
        elif self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn4.text and self.root.ids.btn4.text == self.root.ids.btn7.text:
            return self.end_game(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)

        elif self.root.ids.btn2.text != "" and self.root.ids.btn2.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn8.text:
            return self.end_game(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)

        elif self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn6.text and self.root.ids.btn6.text == self.root.ids.btn9.text:
            return self.end_game(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

        # Diagonal 
        elif self.root.ids.btn1.text != "" and self.root.ids.btn1.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn9.text:
            return self.end_game(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)

        elif self.root.ids.btn3.text != "" and self.root.ids.btn3.text == self.root.ids.btn5.text and self.root.ids.btn5.text == self.root.ids.btn7.text:
            return self.end_game(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

        else:
            self.no_winner()


    # check if its a tie
    def no_winner(self):
        if self.winner == False and \
        self.root.ids.btn1.disabled == True and \
        self.root.ids.btn2.disabled == True and \
        self.root.ids.btn3.disabled == True and \
        self.root.ids.btn4.disabled == True and \
        self.root.ids.btn5.disabled == True and \
        self.root.ids.btn6.disabled == True and \
        self.root.ids.btn7.disabled == True and \
        self.root.ids.btn8.disabled == True and \
        self.root.ids.btn9.disabled == True:
            self.root.ids.score.color = "orange"
            self.root.ids.score.text = "IT'S A TIE!!"

    def disable_all_buttons(self):
        self.root.ids.btn1.disabled = True
        self.root.ids.btn2.disabled = True
        self.root.ids.btn3.disabled = True
        self.root.ids.btn4.disabled = True
        self.root.ids.btn5.disabled = True
        self.root.ids.btn6.disabled = True
        self.root.ids.btn7.disabled = True
        self.root.ids.btn8.disabled = True
        self.root.ids.btn9.disabled = True
    
    def reset_btn_colors(self):
        self.root.ids.btn1.color = "green"
        self.root.ids.btn2.color = "green"
        self.root.ids.btn3.color = "green"
        self.root.ids.btn4.color = "green"
        self.root.ids.btn5.color = "green"
        self.root.ids.btn6.color = "green"
        self.root.ids.btn7.color = "green"
        self.root.ids.btn8.color = "green"
        self.root.ids.btn9.color = "green"

        self.root.ids.btn1.background_color = "green"
        self.root.ids.btn2.background_color = "green"
        self.root.ids.btn3.background_color = "green"
        self.root.ids.btn4.background_color = "green"
        self.root.ids.btn5.background_color = "green"
        self.root.ids.btn6.background_color = "green"
        self.root.ids.btn7.background_color = "green"
        self.root.ids.btn8.background_color = "green"
        self.root.ids.btn9.background_color = "green"


    def restart(self):
        # reset btn colors
        self.reset_btn_colors()
        
        # enable all buttons
        self.root.ids.btn1.disabled = False
        self.root.ids.btn2.disabled = False
        self.root.ids.btn3.disabled = False
        self.root.ids.btn4.disabled = False
        self.root.ids.btn5.disabled = False
        self.root.ids.btn6.disabled = False
        self.root.ids.btn7.disabled = False
        self.root.ids.btn8.disabled = False
        self.root.ids.btn9.disabled = False

        # clear all buttons
        self.root.ids.btn1.text =""
        self.root.ids.btn2.text =""
        self.root.ids.btn3.text =""
        self.root.ids.btn4.text =""
        self.root.ids.btn5.text =""
        self.root.ids.btn6.text =""
        self.root.ids.btn7.text =""
        self.root.ids.btn8.text =""
        self.root.ids.btn9.text =""

        # reset score text
        self.root.ids.score.color = "white"
        self.root.ids.score.text = "X goes first!"
        # reset winner
        self.winner = False
        # reset turn
        self.turn = "X"
    
    # end the current game (notice NOT exit the game, just end the "session")
    def end_game(self, a, b, c):
        a.color = "green"
        b.color = "green"
        c.color = "green"
        a.elevation = 6
        b.elevation = 6
        c.elevation = 6
        c.background_color = "yellow"
        a.background_color = "yellow"
        b.background_color = "yellow"
        self.winner = True
        self.disable_all_buttons()
        self.root.ids.score.color = "green"
        self.root.ids.score.text = f"{a.text} Wins!\nClick 'Restart Game' to start a new round."

        if (a.text == "X"):
            self.X_win += 1
        else:
            self.O_win += 1
        self.root.ids.game.text = f"X-Wins: {self.X_win} | O-Wins: {self.O_win}"

    # exit the app
    def exit_game(self):
        app.stop()
        exit(0)

    def reset_score(self):
        self.root.ids.game.text = "X-Wins: 0 | O-Wins: 0"

if __name__=="__main__":
    app = GameApp()
    try:
        app.run()
    except (KeyboardInterrupt, SystemExit):
        print("Kivy app closed")
        exit(0)